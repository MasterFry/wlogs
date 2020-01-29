from ..EventType import EventType
from .AEventAdvancedSpell import AEventAdvancedSpell
from .A2EventDamage import A2EventDamage
from ..EventParser import EventParser

class EventRangeDamage(AEventAdvancedSpell, A2EventDamage):
    def __init__(self, time, parser: EventParser):
        AEventAdvancedSpell.__init__(self, time, EventType.RANGE_DAMAGE, parser)
        A2EventDamage.__init__(self, EventType.RANGE_DAMAGE, parser)

    def encode(self, encoder) -> bytes:
        return AEventAdvancedSpell.encode(encoder) + A2EventDamage.encode(encoder)

    def __str__(self):
        return AEventAdvancedSpell.__str__(self) + A2EventDamage.__str__(self)

    def __eq__(self, other):
        return AEventAdvancedSpell.__eq__(other) and A2EventDamage.__str__(self)
        
    def __ne__(self, other):
        return not self.__eq__(other)

