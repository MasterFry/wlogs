
from ..types import EventType
from ..encode.AEncoder import AEncoder

from ..EventParser import EventParser

from .A2EventDamage import A2EventDamage
from .AEventAdvancedSpell import AEventAdvancedSpell

class EventRangeDamage(AEventAdvancedSpell, A2EventDamage):
    def __init__(self, time, parser):
        AEventAdvancedSpell.__init__(self, time, EventType.RANGE_DAMAGE, parser)
        A2EventDamage.__init__(self, EventType.RANGE_DAMAGE, parser)

    def encode(self, encoder: AEncoder) -> bytes:
        return AEventAdvancedSpell.encode(self, encoder) + A2EventDamage.encode(self, encoder)

    def __str__(self):
        return AEventAdvancedSpell.__str__(self) + A2EventDamage.__str__(self)

    def __eq__(self, other):
        return AEventAdvancedSpell.__eq__(self, other) and A2EventDamage.__str__(self)
        
    def __ne__(self, other):
        return not self.__eq__(other)

