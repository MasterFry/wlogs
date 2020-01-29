from ..EventType import EventType
from .AEventBase import AEventBase
from .AEventAdvanced import AEventAdvanced
from .A2EventDamage import A2EventDamage
from ..EventParser import EventParser

class EventSwingDamageLanded(AEventAdvanced, A2EventDamage):
    def __init__(self, time, parser: EventParser):
        AEventBase.__init__(self, time, EventType.SWING_DAMAGE_LANDED, parser)
        AEventAdvanced.__init__(self, parser)
        A2EventDamage.__init__(self, EventType.SWING_DAMAGE_LANDED, parser)

    def encode(self, encoder) -> bytes:
        return AEventBase.encode(encoder) + AEventAdvanced.encode(encoder) + A2EventDamage.encode(encoder)

    def __str__(self):
        return AEventBase.__str__(self) + AEventAdvanced.__str__(self) + A2EventDamage.__str__(self)

    def __eq__(self, other):
        return AEventAdvanced.__eq__(other) and A2EventDamage.__eq__(other)
        
    def __ne__(self, other):
        return not self.__eq__(other)

