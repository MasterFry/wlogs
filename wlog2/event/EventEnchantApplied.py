
from ..types import EventType

from ..EventParser import EventParser

from .A2EventEnchant import A2EventEnchant
from .AEventBaseSpell import AEventBaseSpell

class EventEnchantApplied(AEventBaseSpell, A2EventEnchant):
    def __init__(self, time, parser):
        AEventBaseSpell.__init__(self, time, EventType.ENCHANT_APPLIED, parser)
        A2EventEnchant.__init__(self, EventType.ENCHANT_APPLIED, parser)

    def encode(self, encoder: AEncoder) -> bytes:
        return AEventBaseSpell.encode(self, encoder: AEncoder) + A2EventEnchant.encode(self, encoder: AEncoder)

    def __str__(self):
        return AEventBaseSpell.__str__(self) + A2EventEnchant.__str__(self)

    def __eq__(self, other):
        return AEventBaseSpell.__eq__(other) and A2EventEnchant.__eq__(other)
        
    def __ne__(self, other):
        return not self.__eq__(other)

