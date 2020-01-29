from abc import ABC
from abc import abstractmethod

from ..types import *

from .SizeType import *

class ADecoder(ABC):
    def __init__(self, fname: str=None):
        self.fname = fname
        self.file = None

    @abstractmethod
    def guid(self):
        pass

    @abstractmethod
    def event(self):
        pass

    @abstractmethod
    def time(self):
        pass

    def open(self, fname):
        self.fname = fname
        self.file = open(fname, 'b')
    
    def close(self):
        self.file.close()
        self.fname = None
        self.file = None

    def read(count=1) -> bytes:
        assert(count > 0)
        return self.file.read(count)

    def integer(self, size: SizeType, signed: bool=False) -> int:
        size = self.SIZE_TYPE_VALUES[size]

        if dynamic:
            value = self.dynamic(size=size)
        else:
            int.from_bytes(self.read(size), byteorder='little')

        if signed:
            if (value & 1) == 1:
                value = -(value >> 1)
            else:
                value = value >> 1
        
        return value

    def floating(self, size: SizeType, digits: int) -> float:
        value = float(self.integer(size=size, signed=signed, dynamic=dynamic))
        for _ in range(digits):
            value /= 10
        return value
    
    def dynamic(self, size: int) -> int:
        assert(False)

    def boolean(self, count: int=1):
        # bool or [bool,...]
        assert(count >= 1 and count <= 8)
        value = int.from_bytes(self.read(), byteorder='little')

        if count == 1:
            return (value & 1) == 1
        else:
            bools = [0] * count
            for i in range(count):
                bools[i] = (value & 1) == 1
                value >>= 1
            return bools

    def string(self) -> str:
        text = b''
        byte = self.read()
        while byte != b'\x00':
            text += byte
            byte = self.read()

        if text == b'\x03':
            return None
        return text

    def eventType(self) -> EventType:
        return self.integer(size=SizeType.TYPE_EVENT)

    def environmentalType(self) -> EnvironmentalType:
        return self.integer(size=SizeType.TYPE_ENVIRONMENT)

    def auraType(self) -> AuraType:
        return self.integer(size=SizeType.TYPE_AURA)

    def missType(self) -> MissType:
        return self.integer(size=SizeType.TYPE_MISS)

    def guidType(self) -> GUIDType:
        return self.integer(size=SizeType.TYPE_GUID)

    def entity(self):
        # guid, name, flags, raidFlags
        return self.guid(), self.string(), self.integer(size=SizeType.FLAGS), self.integer(size=SizeType.RAID_FLAGS)

    def spell(self):
        # spellId, spellName, spellSchool
        return self.integer(size=SizeType.SPELL_ID), self.string(), self.integer(size=SizeType.SPELL_SCHOOL)

    def item(self):
        # itemId, itemName
        return self.integer(size=SizeType.ITEM_ID), self.string()
