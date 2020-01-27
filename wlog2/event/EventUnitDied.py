from ..EventType import EventType
from .AEventBase import AEventBase
from ..EventParser import EventParser

class EventUnitDied(AEventBase):
    def __init__(self, time, eventType, parser: EventParser):
        AEventBase.__init__(self, time, EventType.UNIT_DIED, parser)
        self.recapId = parser.getInt(base=16)
        self.unconsciousOnDeath = parser.getInt(base=16)
        assert(False)

    def __str__(self):
        return AEventBase.__str__(self) + ',{0:#x},{1:#x}'.format(
            self.recapId,
            self.unconsciousOnDeath
        )

    def __eq__(self, other):
        return AEventBase.__eq__(other)       and \
               self.recapId == other.recapId and \
               self.unconsciousOnDeath == other.unconsciousOnDeath
        
    def __ne__(self, other):
        return not self.__eq__(other)

