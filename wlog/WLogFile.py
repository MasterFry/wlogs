from .Buffs import PlayerBuffs
from .Buffs import BuffLogFile
from .Encounter import Encounter
from .Event import Event
from .GUID import GUID
from .Time import Time
from .Time import TIME_EPSILON_CMP_ENCOUNTER
from .UnitFlag import UnitFlag

from .Utils import CorruptionError
from .Utils import wlog_split_line

import numpy as np

# COMBATANT_INFO
# 10/29 18:08:40.614  COMBAT_LOG_VERSION,9,ADVANCED_LOG_ENABLED,1,BUILD_VERSION,1.13.2,PROJECT_ID,2
#
# 11/6 20:56:27.184  SPELL_AURA_APPLIED,Player-4701-008F0D39,"Madretsma-Mograine",0x514,0x0,Player-4701-008F0D39,"Madretsma-Mograine",0x514,0x0,15359,"Inspiration",0x2,BUFF
#                                       caster of aura                                      applied to
# 11/6 20:40:39.421  SPELL_AURA_APPLIED_DOSE,Player-4701-00B8EC93,"Elveren-Mograine",0x40512,0x0,Creature-0-4448-409-26194-12098-000043171A,"Sulfuron Harbinger",0xa48,0x0,11597,"Sunder Armor",0x1,DEBUFF,2
# 11/6 20:56:27.184  SPELL_AURA_BROKEN,Player-4701-009A42DA,"Jettesnell-Mograine",0x40512,0x0,Creature-0-4448-409-26194-11663-0000C33261,"Flamewaker Healer",0xa48,0x40,12826,"Polymorph",0x40,DEBUFF
# 11/6 20:43:05.077  SPELL_AURA_BROKEN_SPELL,Creature-0-4448-409-26194-11673-0000C3171A,"Ancient Core Hound",0x10a48,0x0,Player-4701-0090D265,"Ylrem-Mograine",0x514,0x0,1787,"Stealth",0x1,21333,"Lava Breath",4,BUFF
# 11/6 20:56:27.184  SPELL_AURA_REMOVED,Player-4701-00DFC624,"Sublimit-Mograine",0x514,0x0,Creature-0-4448-409-26194-11663-0000C33261,"Flamewaker Healer",0xa48,0x40,12826,"Polymorph",0x40,DEBUFF
#                                       caster of aura                                     removed from
# 11/6 20:40:34.556  SPELL_AURA_REMOVED_DOSE,Player-4701-008838B8,"Jexx-Mograine",0x40511,0x0,Player-4701-008838B8,"Jexx-Mograine",0x40511,0x0,2565,"Shield Block",0x1,BUFF,1

class WLogFile:
    def __init__(self, fname: str):
        self.fname = fname
        self.time = None
        self.init_line = None
        self.encounters = None
        self.loggerGUID = None
        self.loggerName = None
        self.buffLogFile = BuffLogFile('')

    def setBuffLogFile(self, buffLogFile: BuffLogFile):
        self.buffLogFile = buffLogFile

    def findGUID(self, name):
        for encounter in self.encounters:
            for event in encounter.events:
                print(event.srcName)
                return None
                if event.srcGUID !=  name == event.srcName:
                    return event.srcGUID
                if name == event.destName:
                    return event.destGUID
        return None

    def merge(self, other):
        assert(isinstance(other, WLogFile))

        print('Merging %s into %s...' % (other.fname, self.fname))

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
            elif matrix[i1][i2] == matrix[i1][i2 - 1]:
                self.encounters.insert(i1, self.convertEncounter(other.init_time, other.encounters[i2]))
                i2 -= 1
            else:
                i1 -= 1

        print('Done merging %s into %s' % (other.fname, self.fname))

    def load(self):
        print('Loading from %s...' % self.fname)
        with open(self.fname) as file:
            try:
                self.__load(file)
                print('Done Loading %s' % self.fname)
            except CorruptionError:
                print('Corruption in File %s detected' % self.fname)

    def __load(self, file):
        # advreq: Advanced Combat Logging Required:
        #         Throws an Error if <advreq> is True and advanced combat logging is not enabled

        # check init line
        self.init_line = file.readline()
        init_params = wlog_split_line(self.init_line)
        if init_params[5] != 'COMBAT_LOG_VERSION':
            raise ValueError("Log File doesn't start with COMBAT_LOG_VERSION")
        if int(init_params[8]) == 0:
            raise AdvancedLoggingError()
        self.time = Time(init_params)

        FAKED_ADVANCED_PARAMS = 0
        
        # load encounters
        buffs = PlayerBuffs()
        self.encounters = list()
        encounter = self.loadEncounter(file, buffs)
        while encounter is not None:
            self.encounters.append(encounter)
            encounter = self.loadEncounter(file, buffs)

        if len(self.encounters) == 0:
            print('No Encounters found!')
            return
        
        # find logging player
        for encounter in self.encounters:
            for event in encounter.events:
                if UnitFlag.isMine(event.srcFlags):
                    self.loggerGUID = event.srcGUID
                    self.loggerName = event.srcName
                    break
                if UnitFlag.isMine(event.destFlags):
                    self.loggerGUID = event.destGUID
                    self.loggerName = event.destName
                    break
        
        if self.loggerGUID is None:
            raise ValueError("Logger NOT found!")

    def loadEncounter(self, file, buffs: PlayerBuffs):
        events = list()
        combat_info = list()
        start_params = None
        end_params = None

        # find the start of the encounter
        line = file.readline()
        while line != '':
            params = wlog_split_line(line)
            if Encounter.isStart(params):
                start_params = params
                break
            
            if params[5] == 'COMBAT_LOG_VERSION':
                raise ValueError("Log File contains multiple Logs!") # TODO

            # track buffs
            event = Event(params)
            if self.buffLogFile.peek().time < event.time:
                buffs.load(self.buffLogFile.next())
            elif UnitFlag.isPlayer(event.destFlags) and not UnitFlag.isOutsider(event.destFlags):
                if event.event == 'SPELL_AURA_APPLIED'      or \
                   event.event == 'SPELL_AURA_APPLIED_DOSE' or \
                   event.event == 'SPELL_AURA_REFRESH':
                    buffs.set(event.time, event.srcGUID, event.destGUID, event.prefix_params[0])
                elif event.event == 'SPELL_AURA_BROKEN'       or \
                     event.event == 'SPELL_AURA_BROKEN_SPELL' or \
                     event.event == 'SPELL_AURA_REMOVED'      or \
                     event.event == 'SPELL_AURA_REMOVED_DOSE':
                    buffs.unset(event.time, event.destGUID, event.prefix_params[0])
                elif event.event == 'UNIT_DIED'       or \
                     event.event == 'SPELL_INSTAKILL':
                    buffs.unsetAll(event.time, event.destGUID)

            line = file.readline()
        if start_params is None:
            return None

        combatants = dict() # playerGUID => (COMBATANT_INFO - line, buffs)

        # read the combatant info
        line = file.readline()
        while line != '':
            params = wlog_split_line(line)
            
            if params[5] == 'COMBAT_LOG_VERSION':
                raise ValueError("Log File contains multiple Logs!")

            if not Encounter.isCombatantInfo(params):
                break
            if line[-3:-1] != '[]':
                # for i in range(1, 5):
                #     print(ord(line[-i]))
                raise ValueError('Is the BUFFS section in COMBATANT_INFO being filled now?')
            combatants[params[6]] = (line[:-3], buffs.copy(params[6]))
            # combat_info.append(line[:-3])
            line = file.readline()

        # this will be used to fill the COMBATANT_INFO sections
        # start_buffs = buffs.copy()
            
        # load events until the end of the encounter
        # line = file.readline()
        while line != '':
            params = wlog_split_line(line)
            
            if params[5] == 'COMBAT_LOG_VERSION':
                raise ValueError("Log File contains multiple Logs!")

            if Encounter.isEnd(params):
                end_params = params
                break
            if Encounter.isStart(params):
                raise CorruptionError
            if Encounter.isCombatantInfo(params):
                raise ValueError('COMBATANT_INFO not next to ENCOUNTER_START')
            else:
                event = Event(params)
                events.append(event)
                
                # track buffs for later encounters
                if self.buffLogFile.peek().time < event.time:
                    buffs.load(self.buffLogFile.next())
                elif UnitFlag.isPlayer(event.destFlags) and not UnitFlag.isOutsider(event.destFlags):
                    if event.event == 'SPELL_AURA_APPLIED' or \
                       event.event == 'SPELL_AURA_APPLIED_DOSE':
                        buffs.set(event.time, event.srcGUID, event.destGUID, event.prefix_params[0])
                    elif event.event == 'SPELL_AURA_BROKEN'       or \
                         event.event == 'SPELL_AURA_BROKEN_SPELL' or \
                         event.event == 'SPELL_AURA_REMOVED'      or \
                         event.event == 'SPELL_AURA_REMOVED_DOSE':
                        buffs.unset(event.time, event.destGUID, event.prefix_params[0])
                    elif event.event == 'UNIT_DIED':
                        buffs.unsetAll(event.time, event.destGUID)

            line = file.readline()
        
        if end_params is None:
            raise ValueError("End of Encounter NOT found!")
        
        # return Encounter(start_params, end_params, events, combat_info, start_buffs)
        return Encounter(start_params, end_params, events, combatants)

    def convertEncounter(self, init_time, encounter):
        # time offset from other to self
        time_offset = (self.time - init_time).time

        # find self's party members
        # partyGUIDs = list()
        # for event in self.events:
        #     if UnitFlag.isParty(event.srcFlags):
        #         if event.srcGUID not in partyGUIDs:
        #             partyGUIDs.append(event.srcGUID)
        #     if UnitFlag.isParty(event.destFlags):
        #         if event.destGUID not in partyGUIDs:
        #             partyGUIDs.append(event.destGUID)
        #     if len(partyGUIDs) == 4:
        #         break

        # update other.events
        for event in other.events:
            # update srcFlags
            if event.srcGUID == self.loggerGUID:
                event.srcFlags = UnitFlag.setMine(event.srcFlags)
            elif UnitFlag.isMine(event.srcFlags):
                event.srcFlags = UnitFlag.setRaid(event.srcFlags)
            # elif event.srcGUID in partyGUIDs:
            #     if not UnitFlag.isOutsider(event.srcFlags):
            #         event.srcFlags = UnitFlag.setParty(event.srcFlags)
            # elif event.srcGUID not in partyGUIDs:
            #     if not UnitFlag.isOutsider(event.srcFlags):
            #         event.srcFlags = UnitFlag.setRaid(event.srcFlags)
            # update destFlags
            if event.destGUID == self.loggerGUID:
                event.destFlags = UnitFlag.setMine(event.destFlags)
            elif UnitFlag.isMine(event.destFlags):
                event.destFlags = UnitFlag.setRaid(event.destFlags)
            # elif event.destGUID in partyGUIDs:
            #     if not UnitFlag.isOutsider(event.destFlags):
            #         event.destFlags = UnitFlag.setParty(event.destFlags)
            # elif event.destGUID not in partyGUIDs:
            #     if not UnitFlag.isOutsider(event.destFlags):
            #         event.destFlags = UnitFlag.setRaid(event.destFlags)
            # update time
            event.time += time_offset
    
    def save(self, fname: str):
        assert(self.encounters is not None)
        print('Saving to %s...' % fname)
        with open(fname, 'w') as file:
            file.write(self.init_line)
            for encounter in self.encounters:
                encounter.writeTo(file)
        print('Done Saving %s' % fname)
