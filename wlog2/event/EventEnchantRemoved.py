
from ..types import EventType
from ..encode.AEncoder import AEncoder

from ..EventParser import EventParser

from .A2EventEnchant import A2EventEnchant
from .AEventBase import AEventBase

class EventEnchantRemoved(AEventBase, A2EventEnchant):
    def __init__(self, time, parser):
        AEventBase.__init__(self, time, EventType.ENCHANT_REMOVED, parser)
        A2EventEnchant.__init__(self, EventType.ENCHANT_REMOVED, parser)

    def encode(self, encoder: AEncoder) -> bytes:
        return AEventBase.encode(self, encoder) + A2EventEnchant.encode(self, encoder)

    def __str__(self):
        return AEventBase.__str__(self) + A2EventEnchant.__str__(self)

    def __eq__(self, other):
        return AEventBase.__eq__(self, other) and A2EventEnchant.__eq__(self, other)
        
    def __ne__(self, other):
        return not self.__eq__(other)

