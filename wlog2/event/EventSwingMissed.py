
from ..types import EventType
from ..encode.AEncoder import AEncoder

from ..EventParser import EventParser

from .A2EventMissed import A2EventMissed
from .AEventBase import AEventBase

class EventSwingMissed(AEventBase, A2EventMissed):
    def __init__(self, time, parser):
        AEventBase.__init__(self, time, EventType.SWING_MISSED, parser)
        A2EventMissed.__init__(self, EventType.SWING_MISSED, parser)

    def encode(self, encoder: AEncoder) -> bytes:
        return AEventBase.encode(self, encoder) + A2EventMissed.encode(self, encoder)

    def __str__(self):
        return AEventBase.__str__(self) + A2EventMissed.__str__(self)

    def __eq__(self, other):
        return AEventBase.__eq__(self, other) and A2EventMissed.__eq__(self, other)
        
    def __ne__(self, other):
        return not self.__eq__(other)

