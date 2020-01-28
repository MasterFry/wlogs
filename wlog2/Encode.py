from enum import IntEnum

from wlog import Time
from wlog import GUID

from .AuraType import AuraType
from .EnvironmentalType import EnvironmentalType
from .EventType import EventType
from .MissType import MissType

class SizeType(IntEnum):
    ALTERNATE_POWER_TYPE  = 0
    AURA_AMOUNT           = 1
    COMBATANT_STATS       = 2
    COMBATLOG_PROJECT_ID  = 3
    COMBATLOG_VERSION     = 4
    COORDINATE            = 5
    DIFFICULTY_ID         = 6
    DMG_AMOUNT            = 7
    DMG_P2                = 8
    DMG_P3                = 9
    ENCOUNTER_ID          = 10
    ENCOUNTER_START_P4    = 11
    ENERGIZE_AMOUNT       = 12
    EXTRA_ATTACK_AMOUNT   = 13
    FACING                = 14
    FLAGS                 = 15
    HEAL_AMOUNT           = 16
    HEAL_P1               = 17
    HP                    = 18
    ITEM_ID               = 19
    LEVEL                 = 20
    MISSED_AMOUNT         = 21
    MISSED_CRITICAL       = 22
    PLAYER_COUNT          = 23
    POWER_TYPE            = 24
    RAID_FLAGS            = 25
    SPELL_ABSORBED_AMOUNT = 26
    SPELL_ABSORBED_P5     = 27
    SPELL_ID              = 28
    SPELL_SCHOOL          = 29
    MAP_ID                = 30


class Encoder:
    def __init__(self):
        # Load the Size Types
        self.sizeTypeChanged = False
        sizeTypeNames = [SizeType(x).name for x in range(len(SizeType))]
        self.sizeTypeValues = [1] * len(sizeTypeNames)
        with open('SizeType.txt') as file:
            line = file.readline()
            while line != '':
                r = line.split('=')
                sizeType = sizeTypeNames.index(r[0])
                self.sizeTypeValues[sizeType] = int(r[1])
                line = file.readline()

    def __del__(self):
        # Save the Size Types
        if self.sizeTypeChanged:
            with open('SizeType.txt', 'w') as file:
                for i in range(len(SizeType)):
                    file.write('%s=%d\n' % (SizeType(i).name, self.sizeTypeValues(i)))

    def integer(self, value: int, size: SizeType, signed: bool=False) -> bytes:
        if signed:
            if value < 0:
                value = ((-value) << 1) | 1
            else:
                value = (value << 1)
        elif value < 0:
            raise ValueError('Negative value with signed set to False!')

        while value >= (256 ** self.sizeTypeValues[size]):
            self.sizeTypeValues[size] += 1
            self.sizeTypeChanged = True

        return value.to_bytes(length=self.sizeTypeValues[size], byteorder='little')

    def floating(self, value: float, size: SizeType, digits: int, signed: bool=False) -> bytes:
        for _ in range(digits):
            value *= 10
        return self.integer(int(value), size=size, signed=signed)

    def dynamic(self, value: int, size: int) -> bytes:
        pass

    def eventType(self, eventType: EventType) -> bytes:
        return encodeInt(int(eventType), size=1)

    def environmentalType(self, environmentalType: EnvironmentalType) -> bytes:
        return encodeInt(int(environmentalType), size=1)

    def auraType(self, auraType: AuraType) -> bytes:
        return encodeInt(int(auraType), size=1)

    def missType(self, missType: MissType) -> bytes:
        return encodeInt(int(missType), size=1)

    def time(self, time: Time) -> bytes:
        return time.encode()

    def guid(self, guid: GUID) -> bytes:
        pass

    def entity(self, guid: GUID, name: str, flags: int, raidFlags: int) -> bytes:
        pass

    def spell(self, spellId: int, spellName: str, spellSchool: int) -> bytes:
        pass

    def item(self, itemId: int, itemName: str) -> bytes:
        pass

    def string(self, string: str) -> bytes:
        return string.encode(encoding='utf-8') + bytes(1)

    def boolean(self, boolean) -> bytes:
        if isinstance(boolean, bool):
            return b'\x01' if boolean else b'\x00'
        if isinstance(boolean, list):
            value = 0
            for b in boolean:
                value = (value << 1) | b
            return self.dynamic(value, size=1)
        raise ValueError('Invalid value for boolean(s): ' + str(boolean))

    
