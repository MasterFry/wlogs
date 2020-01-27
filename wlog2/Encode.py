from wlog import Time
from wlog import GUID

class Encoder:
    def __init__(self):
        pass

    def integer(self, value: int, size: int, signed=False: bool) -> bytes:
        return value.to_bytes(length=size, byteorder='little')

    def floating(self, value: float, size: int, digits: int, signed=False: bool) -> bytes:
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
        pass

    def boolean(self, boolean) -> bytes:
        assert(isinstance(boolean, bool) or isinstance(boolean, list))
        pass

    
