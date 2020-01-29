
from ..types import EventType

from ..EventParser import EventParser

from .A2EventDamage import A2EventDamage
from .AEventAdvanced import AEventAdvanced
from .AEventBase import AEventBase

class EventSwingDamage(AEventAdvanced, A2EventDamage):
    def __init__(self, time, parser):
        AEventBase.__init__(self, time, EventType.SWING_DAMAGE, parser)
        AEventAdvanced.__init__(self, parser)
        A2EventDamage.__init__(self, EventType.SWING_DAMAGE, parser)

    def encode(self, encoder: Encoder) -> bytes:
        return AEventBase.encode(self, encoder: Encoder) + AEventAdvanced.encode(self, encoder: Encoder) + A2EventDamage.encode(self, encoder: Encoder)

    def __str__(self):
        return AEventBase.__str__(self) + AEventAdvanced.__str__(self) + A2EventDamage.__str__(self)

    def __eq__(self, other):
        return AEventAdvanced.__eq__(other) and A2EventDamage.__eq__(self)
        
    def __ne__(self, other):
        return not self.__eq__(other)

