
from ..types import EventType

from ..EventParser import EventParser

from .A2EventMissed import A2EventMissed
from .AEventBase import AEventBase

class EventSwingMissed(AEventBase, A2EventMissed):
    def __init__(self, time, parser: EventParser):
        AEventBase.__init__(self, time, EventType.SWING_MISSED, parser)
        A2EventMissed.__init__(self, EventType.SWING_MISSED, parser)

    def encode(self, encoder) -> bytes:
        return AEventBase.encode(self, encoder) + A2EventMissed.encode(self, encoder)

    def __str__(self):
        return AEventBase.__str__(self) + A2EventMissed.__str__(self)

    def __eq__(self, other):
        return AEventBase.__eq__(self) and A2EventMissed.__eq__(self)
        
    def __ne__(self, other):
        return not self.__eq__(other)

