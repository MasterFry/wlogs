import numpy as np

from wlog import UnitFlag
from .Time import Time
from wlog import TIME_EPSILON_CMP_ENCOUNTER

from .BuffTracker import BuffTracker
from .WLogParser import WLogParser
from .Encounter import Encounter
from .types import *


class CorruptionError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class WLog:
    def __init__(self, fname: str):
        self.fname = fname
        self.logVersion = None
        self.eventBlocks = None
        self.encounters = None
        self.loggerGUID = None

    def merge(self, other):
        assert(isinstance(other, WLog))

        print('[WLOG]: Merging %s <== %s...' % (self.fname, other.fname))

        # use a specific time epsilon for comparing encounters
        Time.setEpsilon(TIME_EPSILON_CMP_ENCOUNTER)

        # find common encounters
        matrix = np.zeros((len(self.encounters) + 1, len(other.encounters) + 1), dtype=np.uint32)
        for i1 in range(1, len(self.encounters) + 1):
            for i2 in range(1, len(other.encounters) + 1):
                if self.encounters[i1 - 1] == other.encounters[i2 - 1]:
                    matrix[i1][i2] = matrix[i1 - 1][i2 - 1] + 1
                else:
                    matrix[i1][i2] = max(matrix[i1 - 1][i2], matrix[i1][i2 - 1])
          
        Time.resetEpsilon()

        # TODO offset comparison ALG

        # merge encounter lists
        i1 = len(self.encounters)
        i2 = len(other.encounters)
        encounters = list()
        while i1 > 0 and i2 > 0:
            if self.encounters[i1 - 1] == other.encounters[i2 - 1]:
                self.encounters[i1 - 1].merge(other.encounters[i2 - 1], self.loggerGUID, other.loggerGUID)
                i1 -= 1
                i2 -= 1
            # elif matrix[i1][i2] == matrix[i1][i2 - 1]:
            #     self.encounters.insert(i1, self.convertEncounter(other.init_time, other.encounters[i2]))
            #     i2 -= 1
            else:
                assert(False and 'Needs to be tested!')
                # i1 -= 1

        print('[WLOG]: Done merging %s <== %s.' % (self.fname, other.fname))
    
    def save(self, fname: str):
        assert(self.encounters is not None)
        assert((len(self.encounters) + 1) == len(self.eventBlocks))
        print('[WLOG]: Saving to %s...' % fname)

        with open(fname, 'w') as file:
            file.write(str(self.logVersion))
            file.write('\n')
            for i in range(len(self.encounters)):
                for event in self.eventBlocks[i]:
                    file.write(str(event))
                    file.write('\n')
                self.encounters[i].writeTo(file)
            for event in self.eventBlocks[-1]:
                file.write(str(event))
                file.write('\n')

        print('[WLOG]: Done Saving %s.' % fname)

    def load(self, buffTracker: BuffTracker=None):
        print('[WLOG]: Loading %s...' % self.fname)

        if buffTracker is None:
            buffTracker = BuffTracker()
        
        with WLogParser(self.fname) as parser:
            
            self.logVersion = parser.getEvent()
            assert(self.logVersion.eventType == EventType.COMBAT_LOG_VERSION)

            self.loadEvents(parser, buffTracker)

            for block in self.eventBlocks:

                for event in block:
                    if UnitFlag.isMine(event.srcFlags):
                        self.loggerGUID = event.srcGUID
                        break
                    if UnitFlag.isMine(event.destFlags):
                        self.loggerGUID = event.destGUID
                        break
                
                if self.loggerGUID is not None:
                    break

        print('[WLOG]: Done loading %s.' % self.fname)

    def loadEvents(self, parser: WLogParser, buffTracker: BuffTracker):
        self.eventBlocks = list()
        self.encounters = list()
        
        while parser.hasNext():
            start = None
            end = None
            cinfo = list()
            events = list()

            # load events up to the next encounter
            while parser.hasNext():
                event = parser.getEvent()

                if event.eventType == EventType.ENCOUNTER_START:
                    start = event
                    break
                if event.eventType == EventType.COMBAT_LOG_VERSION or \
                   event.eventType == EventType.COMBATANT_INFO or \
                   event.eventType == EventType.ENCOUNTER_END:
                    raise CorruptionError('Unexcpected %s at line: %d' % (event.eventType.name, parser.lineNumber))
                
                buffTracker.checkEvent(event)
                events.append(event)

            self.eventBlocks.append(events)
            events = list()

            if start is None:
                break
            
            # load combatant info
            while parser.hasNext():
                event = parser.getEvent()

                if event.eventType != EventType.COMBATANT_INFO:
                    break
                    # raise CorruptionError('Unexcpected %s at line: %d' % (event.eventType.name, parser.lineNumber))
                
                event.buffs = buffTracker.getBuffs(event.playerGUID)
                cinfo.append(event)

            if len(cinfo) == 0:
                raise CorruptionError('No COMBATANT_INFO found!')

            # load events of the encounter
            if event.eventType == EventType.ENCOUNTER_END:
                end = event
                break
            if event.eventType == EventType.COMBAT_LOG_VERSION or \
                event.eventType == EventType.COMBATANT_INFO or \
                event.eventType == EventType.ENCOUNTER_START:
                raise CorruptionError('Unexcpected %s at line: %d' % (event.eventType.name, parser.lineNumber))

            buffTracker.checkEvent(event)
            events.append(event)

            while parser.hasNext():
                event = parser.getEvent()

                if event.eventType == EventType.ENCOUNTER_END:
                    end = event
                    break
                if event.eventType == EventType.COMBAT_LOG_VERSION or \
                   event.eventType == EventType.COMBATANT_INFO or \
                   event.eventType == EventType.ENCOUNTER_START:
                    raise CorruptionError('Unexcpected %s at line: %d' % (event.eventType.name, parser.lineNumber))

                buffTracker.checkEvent(event)
                events.append(event)
                
            if end is None:
                print(start)
                print(end)
                raise CorruptionError('Unexcpected end of log file inside an encounter!')

            self.encounters.append(Encounter(start, end, cinfo, events))
