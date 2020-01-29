
from ..types import EventType
from ..encode import AEncoder

from ..EventParser import EventParser

from .AEventBase import AEventBase

class EventUnitDied(AEventBase):
    def __init__(self, time, parser):
        AEventBase.__init__(self, time, EventType.UNIT_DIED, parser)
        # self.recapId = parser.getInt(base=16)
        # self.unconsciousOnDeath = parser.getInt(base=16)

    def encode(self, encoder: AEncoder) -> bytes:
        return AEventBase.encode(self, encoder)

    def __str__(self):
        return AEventBase.__str__(self)
        # return AEventBase.__str__(self) + ',{0:#x},{1:#x}'.format(
        #     self.recapId,
        #     self.unconsciousOnDeath
        # )

    def __eq__(self, other):
        return AEventBase.__eq__(other)
        # return AEventBase.__eq__(other)       and \
        #        self.recapId == other.recapId and \
        #        self.unconsciousOnDeath == other.unconsciousOnDeath
        
    def __ne__(self, other):
        return not self.__eq__(other)

