from .AEvent import AEvent
from ..EventType import EventType
from ..EventParser import EventParser

# 1 : Source GUID
#       Player-4701-00B442E4
# 2 : Source Name
#       "Doncarleon-Mograine"
# 3 : Source Unit Flags
#       0x514
# 4 : Source Raid Flags
#       0x0
# 5 : Destination GUID
#       Creature-0-4469-409-26884-11671-000428A101
# 6 : Destination Name
#       "Core Hound"
# 7 : Destination Unit Flags
#       0xa48
# 8 : Destination Raid Flags
#       0x0

class AEventBase(AEvent):
    def __init__(self, time, eventType, parser: EventParser):
        AEvent.__init__(self, time, eventType)
        self.srcGUID = parser.getGUID()
        self.srcName = parser.getString()
        self.srcFlags = parser.getInt(base=16)
        self.srcRaidFlags = parser.getInt(base=16)
        self.destGUID = parser.getGUID()
        self.destName = parser.getString()
        self.destFlags = parser.getInt(base=16)
        self.destRaidFlags = parser.getInt(base=16)

    def __str__(self):
        return AEvent.__str__(self) + ',{0:s},"{1:s}",{2:#05x},{3:#05x},{4:s},"{5:s}",{6:#05x},{7:#05x}'.format(
            str(self.srcGUID),
            self.srcName,
            self.srcFlags,
            self.srcRaidFlags,
            str(self.destGUID),
            self.destName,
            self.destFlags,
            self.destRaidFlags
        )

    def __eq__(self, other):
        return AEvent.__eq__(other) and \
               self.srcGUID == other.srcGUID and \
               self.destGUID == other.destGUID

    def __ne__(self, other):
        return not self.__eq__(other)