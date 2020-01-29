from wlog import Time

from ..types import *

from .SizeType import *

class AEncoder:
    def __init__(self):
        # self.sizeTypeValues = list(SIZE_TYPE_VALUES)
        self.sizeTypeValues = [1] * len(SizeType)
        self.sizeTypeSums = [0] * len(SizeType)
        self.sizeTypeCounts = [0] * len(SizeType)

    def data(self):
        return self.sizeTypeCounts, self.sizeTypeSums
        # sizeTypeAvgs = [s / c for s, c in zip(self.sizeTypeSums, self.sizeTypeCounts)]
        # for i in range(len(sizeTypeAvgs)):
        #     print(SizeType(i).name, sizeTypeAvgs[i])

    def integer(self, value: int, size: SizeType, signed: bool=False) -> bytes:
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

    def floating(self, value: float, size: SizeType, digits: int, signed: bool=False) -> bytes:
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
            assert(len(list) <= 8)
            value = 0
            for b in boolean:
                value = (value << 1) | b
            return value.to_bytes(1, byteorder='little')
        raise ValueError('Invalid value for boolean(s): ' + str(boolean))

    
