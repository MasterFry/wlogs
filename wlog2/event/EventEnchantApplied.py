from ..EventType import EventType
from .AEventBaseSpell import AEventBaseSpell
from .A2EventEnchant import A2EventEnchant
from ..EventParser import EventParser

class EventEnchantApplied(AEventBaseSpell, A2EventEnchant):
    def __init__(self, time, parser: EventParser):
        AEventBaseSpell.__init__(self, time, EventType.ENCHANT_APPLIED, parser)
        A2EventEnchant.__init__(self, EventType.ENCHANT_APPLIED, parser)

    def __str__(self):
        return AEventBaseSpell.__str__(self) + A2EventEnchant.__str__(self)

    def __eq__(self, other):
        return AEventBaseSpell.__eq__(other) and A2EventEnchant.__eq__(other)
        
    def __ne__(self, other):
        return not self.__eq__(other)

