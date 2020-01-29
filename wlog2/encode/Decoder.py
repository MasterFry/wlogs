from ..types import *

from .SizeTypes import SizeType

class Decoder:
    def __init__(self):
        pass

    def integer(self, size: SizeType, signed: bool=False, dynamic: bool=False) -> int:
        pass

    def floating(self, size: SizeType, digits: int, dynamic: bool=False) -> float:
        pass
    
    def dynamic(self, size: int) -> int:
        assert(False)

    def boolean(self, count: int=1):
        # bool or [bool,...]
        pass

    def string(self) -> str:
        pass

    def eventType(self) -> EventType:
        pass

    def environmentalType(self) -> EnvironmentalType:
        pass

    def auraType(self) -> AuraType:
        pass

    def missType(self) -> MissType:
        pass

    def guidType(self) -> GUIDType:
        pass

    def time(self) -> Time:
        pass

    def guid(self):
        pass

    def entity(self):
        # guid, name, flags, raidFlags
        pass

    def spell(self):
        # spellName, spellId, spellName
        pass

    def item(self):
        # itemId, itemName
        pass
