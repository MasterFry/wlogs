from .Event import Event
from .EventType import EventType
from .EventParser import EventParser

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

class EventBase(Event):
    def __init__(self, time, parser: EventParser):
        Event.__init__(time)
        self.srcGUID = parser.getGUID()
        self.srcName = parser.getString()
        self.srcFlags = parser.getInt(base=16)
        self.srcRaidFlags = parser.getInt(base=16)
        self.destGUID = parser.getGUID()
        self.destName = parser.getString()
        self.destFlags = parser.getInt(base=16)
        self.destRaidFlags = parser.getInt(base=16)

    def __str__(self):
        return Event.__str__(self) + ',' + ','.join([
            str(self.srcGUID),
            '"' + self.srcName + '"',
            '%#05x' % self.srcFlags,
            '%#05x' % self.srcRaidFlags,
            str(self.destGUID),
            '"' + self.destName + '"',
            '%#05x' % self.destFlags,
            '%#05x' % self.destRaidFlags
        ])

    def __eq__(self, other):
        return Event.__eq__(other) and \
               self.srcGUID == other.srcGUID and \
               self.destGUID == other.destGUID

    def __ne__(self, other):
        return not self.__eq__(other)