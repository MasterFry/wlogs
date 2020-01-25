import numpy as np

from .Buffs import PlayerBuffs
from .Time import Time
from .Time import TIME_EPSILON_CMP_ENCOUNTER
from .UnitFlag import UnitFlag

# ['11', '4', '20', '56', '34.043', 'ENCOUNTER_START', '1084', '"Onyxia"', '9', '40', '249']
# ['11', '4', '21', '00', '30.242', 'ENCOUNTER_END', '1084', '"Onyxia"', '9', '40', '1']
class Encounter:
    def __init__(self, start_params, end_params, events, combatants):
        assert(start_params[5] == 'ENCOUNTER_START')
        assert(end_params[5] == 'ENCOUNTER_END')
        assert(start_params[6] == end_params[6])
        self.time_start = Time(start_params)
        self.time_end = Time(end_params)
        self.encounterID   = start_params[6]
        self.encounterName = start_params[7]
        self.difficultyID  = start_params[8]
        self.groupSize     = start_params[9]
        self.unknown_start = start_params[10]
        self.unknown_end   = end_params[10]
        self.events = events
        self.combatants = combatants # playerGUID => (COMBATANT_INFO - line, buffs)
        # self.combat_info = combat_info
        # self.buffs = buffs

    def merge(self, other, selfGUID, otherGUID):
        # Merges <other> into <self>. <self> is the "Main" Encounter when merging.
        assert(isinstance(other, Encounter))
        assert(self.encounterID == other.encounterID)
        Time.setEpsilon(TIME_EPSILON_CMP_ENCOUNTER)
        assert(self.getDuration() == other.getDuration())
        Time.resetEpsilon()
        assert(len(self.events) > 0)
        assert(len(other.events) > 0)

        # time offset from other to self
        time_start_offset = (self.time_start - other.time_start).time
        time_end_offset = (self.time_end - other.time_end).time
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
        for playerGUID in self.combatants:
            PlayerBuffs.merge(self.combatants[playerGUID][1], other.combatants[playerGUID][1])
        # self.buffs.merge(other.buffs)
       
        # calculate the matrix for common events
        matrix = np.zeros((len(self.events) + 1, len(other.events) + 1), dtype=np.uint32)
        # i2Maxima = np.empty((len(other.events) + 1, 1), dtype=np.uint32)
        # i2Maxima[0] = 0
        c = 0
        start = 1
        prevMax = 0
        prevEnd = 1
        for i1 in range(1, len(self.events) + 1):

            # c += 1
            # if c % 100 == 0:
            #     print(c // 100)
            
            while other.events[start - 1].time < self.events[i1 - 1].time:
                start += 1
            for i2 in range(start, prevEnd):
                if self.events[i1 - 1] == other.events[i2 - 1]:
                    # matrix[i1][i2] = i2Maxima[i2 - 1] + 1
                    matrix[i1][i2] = matrix[i1 - 1][i2 - 1] + 1
                    # matrix[i1][i2] = max(prevMax, matrix[i1 - 1][i2 - 1]) + 1
                    # matrix[i1][i2] = prevMax + 1
                    # i2Maxima[i2] = matrix[i1][i2]
                else:
                    matrix[i1][i2] = max(matrix[i1 - 1][i2], matrix[i1][i2 - 1])
                    # i2Maxima[i2] = max(i2Maxima[i2], i2Maxima[i2 - 1])
            prevSet = False
            for i2 in range(prevEnd, len(other.events) + 1):
                if other.events[i2 - 1].time > self.events[i1 - 1].time:
                    prevMax = matrix[i1][i2 - 1]
                    prevEnd = i2
                    prevSet = True
                    break
                if self.events[i1 - 1] == other.events[i2 - 1]:
                    # matrix[i1][i2] = i2Maxima[i2 - 1] + 1
                    matrix[i1][i2] = matrix[i1 - 1][i2 - 1] + 1
                    # matrix[i1][i2] = max(prevMax, matrix[i1 - 1][i2 - 1]) + 1
                    # matrix[i1][i2] = prevMax + 1
                    # i2Maxima[i2] = matrix[i1][i2]
                else:
                    matrix[i1][i2] = max(prevMax, matrix[i1][i2 - 1])
                    # i2Maxima[i2] = max(i2Maxima[i2], i2Maxima[i2 - 1])
            if not prevSet:
                prevEnd = len(other.events) + 1
                prevMax = matrix[i1][len(other.events)]

        
        # print('i2Maxima')
        # print(' '.join([str(int(x)) for x in i2Maxima[0:15]]))
        # print('matrix')
        # for k in range(0, 15):
        #     print(' '.join([str(int(x)) for x in matrix[k][0:15]]))
        # assert(False)
        
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
            assert(i >= 0)
            # if matrix[i1][i2] == 0 and i1 > 200 and i2 > 200:
            #     print(i1, i2)
            #     exit(0)
            if self.events[i1 - 1] == other.events[i2 - 1]:
            # if matrix[i1 - 1][i2] < matrix[i1][i2] and matrix[i1][i2 - 1] < matrix[i1][i2]:
                if (self.events[i1 - 1].srcGUID == otherGUID and self.events[i1 - 1].destGUID != selfGUID) or \
                   (self.events[i1 - 1].destGUID == otherGUID and self.events[i1 - 1].srcGUID != selfGUID):
                    try:
                        events[i] = other.events[i2 - 1]
                    except IndexError:
                        print('IndexError: len(events)=%d, len(self.events)=%d, len(other.events)=%d' % (len(events), len(self.events), len(other.events)))
                        print('DEBUG: i=%d, i1=%d, i2=%d' % (i, i1, i2))
                        raise IndexError
                else:
                    try:
                        events[i] = self.events[i1 - 1]
                    except IndexError:
                        print('IndexError: len(events)=%d, len(self.events)=%d, len(other.events)=%d' % (len(events), len(self.events), len(other.events)))
                        print('DEBUG: i=%d, i1=%d, i2=%d' % (i, i1, i2))
                        raise IndexError
                if not (matrix[i1][i2] == matrix[i1 - 1][i2 - 1] + 1):
                    print(i1, i2, matrix[i1][i2], matrix[i1 - 1][i2 - 1] + 1)
                    assert(False)
                i1 -= 1
                i2 -= 1
                count_common += 1
            elif matrix[i1 - 1][i2] == matrix[i1][i2]:
                try:
                    events[i] = self.events[i1 - 1]
                except IndexError:
                    print('IndexError: len(events)=%d, len(self.events)=%d, len(other.events)=%d' % (len(events), len(self.events), len(other.events)))
                    print('DEBUG: i=%d, i1=%d, i2=%d' % (i, i1, i2))
                    raise IndexError
                if not (matrix[i1][i2] == matrix[i1 - 1][i2]):
                    print(i1, i2, matrix[i1][i2], matrix[i1 - 1][i2])
                    assert(False)
                i1 -= 1
                count_self += 1
                # if count_self > count_common:
                #     print(i1, i2)
                    # return
            else:
                try:
                    events[i] = other.events[i2 - 1]
                except IndexError:
                    print('IndexError: len(events)=%d, len(self.events)=%d, len(other.events)=%d' % (len(events), len(self.events), len(other.events)))
                    print('DEBUG: i=%d, i1=%d, i2=%d' % (i, i1, i2))
                    raise IndexError
                if not (matrix[i1][i2] == matrix[i1][i2 - 1]):
                    print(i1, i2, matrix[i1][i2], matrix[i1][i2 - 1])
                    assert(False)
                i2 -= 1
                count_other += 1
            i -= 1

        print('count_self:', count_self)
        print('count_other:', count_other)
        print('count_common:', count_common)
        print('count_total:', count_self + count_other + count_common)
        assert(common == count_common)
        assert(total == count_self + count_other + count_common)
        
        # assert((i1 == 0 and i2 == 0) or (i1 > 0 and i2 == 0) or (i1 == 0 and i2 > 0))
        # if i1 > 0:
        #     print('NOOOT %d : %d' % (i, i1))
        #     while i >= 0:
        #         events[i] = self.events[i1 - 1]
        #         i1 -= 1
        #         i -= 1
        #         count_self += 1
        # if i2 > 0:
        #     print('NOOOT %d : %d' % (i, i2))
        #     while i >= 0:
        #         events[i] = other.events[i2 - 1]
        #         i2 -= 1
        #         i -= 1
        #         count_other += 1
        # print('count_self:', count_self)
        # print('count_other:', count_other)
        # print('count_common:', count_common)
        # print('count_total:', count_self + count_other + count_common)
        
        # print('DEBUG: i=%d, i1=%d, i2=%d' % (i, i1, i2))
        # count = 0
        # for i in range(len(events)):
        #     if events[i] is None:
        #         count += 1
        #         print(i)
        
        for i in range(len(events)):
            if events[i] is None:
                print('####################### DEBUG #######################')
                print('count:', count)
                print('first:', i)
                print('####################### SELF.EVENTS #######################')
                print('\n'.join([str(x) for x in self.events[:10]]))
                print('####################### OTHER.EVENTS #######################')
                print('\n'.join([str(x) for x in other.events[:10]]))
                print('####################### EVENTS #######################')
                print('\n'.join([str(x) for x in events[:10]]))
                print('####################### MATRIX #######################')
                for k in range(9012 + 15, 9012 - 15, -1):
                    print(' '.join([str(int(x)) for x in matrix[k][8947 - 15:8947 + 15]]))
                assert(False)
        self.events = events
        # TODO
    
    def writeTo(self, file):
        params = [
            self.encounterID,
            self.encounterName,
            self.difficultyID,
            self.groupSize
        ]
        file.write(str(self.time_start) + '  ENCOUNTER_START,' + ','.join(params + [self.unknown_start]) + '\n')
        # write COMBATANT_INFO
        # for line in self.combat_info:
        #     playerGUID = wlog_split_line(line)[6]
        #     file.write(line + self.buffs.getLine(playerGUID) + '\n')
        for playerGUID in self.combatants:
            file.write(self.combatants[playerGUID][0] + PlayerBuffs.toLine(self.combatants[playerGUID][1]) + '\n')
        # write Events
        for event in self.events:
            file.write(str(event))
            file.write('\n')
        file.write(str(self.time_end) + '  ENCOUNTER_END,' + ','.join(params + [self.unknown_end]) + '\n')

    def getDuration(self):
        return self.time_end - self.time_start

    def __eq__(self, other):
        if not isinstance(other, Encounter):
            return False
        if self.encounterID != other.encounterID:
            return False
        if self.getDuration() != other.getDuration():
            return False
        if len(self.combatants) != len(other.combatants):
            return False
        for playerGUID in self.combatants:
            if playerGUID not in other.combatants:
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    @staticmethod
    def isStart(params):
        return params[5] == 'ENCOUNTER_START'

    @staticmethod
    def isEnd(params):
        return params[5] == 'ENCOUNTER_END'

    @staticmethod
    def isCombatantInfo(params):
        return params[5] == 'COMBATANT_INFO'
