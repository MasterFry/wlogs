from enum import IntEnum

from wlog import Time

from .types import *

class SizeType(IntEnum):
    ALTERNATE_POWER_TYPE  = 0
    AURA_AMOUNT           = 1
    COMBATANT_STATS       = 2
    COMBATLOG_PROJECT_ID  = 3
    COMBATLOG_VERSION     = 4
    COORDINATE            = 5
    DIFFICULTY_ID         = 6
    DAMAGE_AMOUNT         = 7
    DAMAGE_P2             = 8
    DAMAGE_P3             = 9
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
    TYPE_EVENT            = 31
    TYPE_ENVIRONMENT      = 32
    TYPE_AURA             = 33
    TYPE_MISS             = 34
    TYPE_GUID             = 35
    GUID_ID               = 36
    GUID_SERVER_ID        = 37
    GUID_INSTANCE_ID      = 38
    GUID_ZONE_UID         = 39
    GUID_SPAWN_UID        = 40
    GUID_PLAYER_UID       = 41
    DRAIN_AMOUNT          = 42
    DRAIN_P6              = 43


class Encoder:
    def __init__(self):
        self.sizeTypeValues = [1] * len(SizeType)
        self.sizeTypeSums = [0] * len(SizeType)
        self.sizeTypeCounts = [0] * len(SizeType)

    def data(self):
        return self.sizeTypeCounts, self.sizeTypeSums
        # sizeTypeAvgs = [s / c for s, c in zip(self.sizeTypeSums, self.sizeTypeCounts)]
        # for i in range(len(sizeTypeAvgs)):
        #     print(SizeType(i).name, sizeTypeAvgs[i])

    def integer(self, value: int, size: SizeType, signed: bool=False, dynamic: bool=False) -> bytes:
        assert(isinstance(size, SizeType))
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
        self.sizeTypeCounts[size] += 1
        self.sizeTypeSums[size] += abs(value)

        if dynamic:
            return self.dynamic(value, size=size)
        return value.to_bytes(length=self.sizeTypeValues[size], byteorder='little')

    def floating(self, value: float, size: SizeType, digits: int, signed: bool=False, dynamic: bool=False) -> bytes:
        for _ in range(digits):
            value *= 10
        return self.integer(int(value), size=size, signed=signed, dynamic=dynamic)

    def dynamic(self, value: int, size: int) -> bytes:
        assert(False)

    def eventType(self, eventType: EventType) -> bytes:
        return self.integer(int(eventType), size=SizeType.TYPE_EVENT)

    def environmentalType(self, environmentalType: EnvironmentalType) -> bytes:
        return self.integer(int(environmentalType), size=SizeType.TYPE_ENVIRONMENT)

    def auraType(self, auraType: AuraType) -> bytes:
        return self.integer(int(auraType), size=SizeType.TYPE_AURA)

    def missType(self, missType: MissType) -> bytes:
        return self.integer(int(missType), size=SizeType.TYPE_MISS)

    def guidType(self, guidType: GUIDType) -> bytes:
        return self.integer(int(guidType), size=SizeType.TYPE_GUID)

    def time(self, time: Time) -> bytes:
        return time.encode()

    def guid(self, guid) -> bytes:
        return guid.encode(self)

    def entity(self, guid, name: str, flags: int, raidFlags: int) -> bytes:
        return self.guid(guid) + self.string(name) + \
            self.integer(flags, size=SizeType.FLAGS) + \
            self.integer(raidFlags, size=SizeType.RAID_FLAGS)

    def spell(self, spellId: int, spellName: str, spellSchool: int) -> bytes:
        return self.integer(spellId, size=SizeType.SPELL_ID) + self.string(spellName) + \
            self.integer(spellSchool, size=SizeType.SPELL_SCHOOL)

    def item(self, itemId: int, itemName: str) -> bytes:
        return self.integer(itemId, size=SizeType.ITEM_ID) + self.string(itemName)

    def string(self, text: str) -> bytes:
        if text == None:
            return b'\x03\x00'
        return text.encode(encoding='utf-8') + b'\x00'

    def boolean(self, boolean) -> bytes:
        if isinstance(boolean, bool):
            return b'\x01' if boolean else b'\x00'
        if isinstance(boolean, list):
            value = 0
            for b in boolean:
                value = (value << 1) | b
            return value.to_bytes(1, byteorder='little')
            # return self.dynamic(value, size=1) TODO
        raise ValueError('Invalid value for boolean(s): ' + str(boolean))

    
