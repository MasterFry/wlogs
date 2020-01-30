import numpy as np

from wlog import UnitFlag
from .Time import Time, TIME_EPSILON_CMP_ENCOUNTER

from .event import *
from .encode import AEncoder
from .encode import ADecoder

from .EventParser import EventParser


class Encounter:
    def __init__(self, start, end, cinfo, events):
        self.start: EventEncounterStart= start
        self.end: EventEncounterEnd= end
        self.cinfo = cinfo
        self.cinfo.sort(key=lambda x: str(x.playerGUID))
        self.events = events

    def getName(self) -> str:
        return self.start.encounterName
        
    def merge(self, other, selfGUID, otherGUID):
        # Merges <other> into <self>. <self> is the "Main" Encounter when merging.
        Time.setEpsilon(TIME_EPSILON_CMP_ENCOUNTER)
        assert(self == other)
        Time.resetEpsilon()
        assert(len(self.events) > 0)
        assert(len(other.events) > 0)

        # time offset from other to self
        time_start_offset = (self.start.time - other.start.time).time
        time_end_offset = (self.end.time - other.end.time).time
        time_offset = (time_start_offset + time_end_offset) / 2

        # find self's party members
        partyGUIDs = list()
        for event in self.events:
            if UnitFlag.isParty(event.srcFlags):
                if event.srcGUID not in partyGUIDs:
                    partyGUIDs.append(event.srcGUID)
            if UnitFlag.isParty(event.destFlags):
                if event.destGUID not in partyGUIDs:
                    partyGUIDs.append(event.destGUID)
            if len(partyGUIDs) == 4:
                break

        # update other.events
        for event in other.events:
            # update srcFlags
            if event.srcGUID == selfGUID:
                event.srcFlags = UnitFlag.setMine(event.srcFlags)
            elif event.srcGUID in partyGUIDs:
                if not UnitFlag.isOutsider(event.srcFlags):
                    event.srcFlags = UnitFlag.setParty(event.srcFlags)
            elif event.srcGUID not in partyGUIDs:
                if not UnitFlag.isOutsider(event.srcFlags):
                    event.srcFlags = UnitFlag.setRaid(event.srcFlags)
            # update destFlags
            if event.destGUID == selfGUID:
                event.destFlags = UnitFlag.setMine(event.destFlags)
            elif event.destGUID in partyGUIDs:
                if not UnitFlag.isOutsider(event.destFlags):
                    event.destFlags = UnitFlag.setParty(event.destFlags)
            elif event.destGUID not in partyGUIDs:
                if not UnitFlag.isOutsider(event.destFlags):
                    event.destFlags = UnitFlag.setRaid(event.destFlags)
            # update time
            event.time += time_offset

        # merge buffs
        for i in range(len(self.cinfo)):
            assert(self.cinfo[i].playerGUID == other.cinfo[i].playerGUID)
            self.cinfo[i].mergeBuffs(other.cinfo[i])
       
        # calculate the matrix for common events
        matrix = np.zeros((len(self.events) + 1, len(other.events) + 1), dtype=np.uint32)
        start = 1
        prevMax = 0
        prevEnd = 1
        for i1 in range(1, len(self.events) + 1):
            while other.events[start - 1].time < self.events[i1 - 1].time:
                start += 1
            for i2 in range(start, prevEnd):
                if self.events[i1 - 1] == other.events[i2 - 1]:
                    matrix[i1][i2] = matrix[i1 - 1][i2 - 1] + 1
                else:
                    matrix[i1][i2] = max(matrix[i1 - 1][i2], matrix[i1][i2 - 1])
            prevSet = False
            for i2 in range(prevEnd, len(other.events) + 1):
                if other.events[i2 - 1].time > self.events[i1 - 1].time:
                    prevMax = matrix[i1][i2 - 1]
                    prevEnd = i2
                    prevSet = True
                    break
                if self.events[i1 - 1] == other.events[i2 - 1]:
                    matrix[i1][i2] = matrix[i1 - 1][i2 - 1] + 1
                else:
                    matrix[i1][i2] = max(prevMax, matrix[i1][i2 - 1])
            if not prevSet:
                prevEnd = len(other.events) + 1
                prevMax = matrix[i1][len(other.events)]

        # merge the event lists
        common = int(matrix[-1][-1])
        total = len(self.events) + len(other.events) - common
        events = [None] * total
        i1 = len(self.events)
        i2 = len(other.events)
        i = len(events) - 1

        print('self:', len(self.events))
        print('other:', len(other.events))
        print('common:', common)
        print('total:', total)

        count_common = 0
        count_self = 0
        count_other = 0
        while i1 > 0 and i2 > 0:
            if self.events[i1 - 1] == other.events[i2 - 1]:
                if (self.events[i1 - 1].srcGUID == otherGUID and self.events[i1 - 1].destGUID != selfGUID) or \
                   (self.events[i1 - 1].destGUID == otherGUID and self.events[i1 - 1].srcGUID != selfGUID):
                    events[i] = other.events[i2 - 1]
                else:
                    events[i] = self.events[i1 - 1]
                i1 -= 1
                i2 -= 1
                count_common += 1
            elif matrix[i1 - 1][i2] == matrix[i1][i2]:
                events[i] = self.events[i1 - 1]
                i1 -= 1
                count_self += 1
            else:
                events[i] = other.events[i2 - 1]
                i2 -= 1
                count_other += 1

            i -= 1
            
        self.events = events

        print('count_self:', count_self)
        print('count_other:', count_other)
        print('count_common:', count_common)
        print('count_total:', count_self + count_other + count_common)
        assert(common == count_common)
        assert(total == count_self + count_other + count_common)

    def writeTo(self, file):
        file.write(str(self.start))
        file.write('\n')
        for event in self.cinfo:
            file.write(str(event))
            file.write('\n')
        for event in self.events:
            file.write(str(event))
            file.write('\n')
        file.write(str(self.end))
        file.write('\n')
    
    def getDuration(self):
        return self.end.time - self.start.time

    def __eq__(self, other):
        if not isinstance(other, Encounter) or \
           self.start.encounterId != other.start.encounterId or \
           self.getDuration() != other.getDuration() or \
           len(self.cinfo) != len(other.cinfo):
            return False
        for cinfo in self.cinfo:
            if not any([cinfo.playerGUID == x.playerGUID for x in other.cinfo]):
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)
