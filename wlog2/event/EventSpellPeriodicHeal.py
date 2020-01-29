
from ..types import EventType
from ..encode import AEncoder

from ..EventParser import EventParser

from .A2EventHeal import A2EventHeal
from .AEventAdvancedSpell import AEventAdvancedSpell

class EventSpellPeriodicHeal(AEventAdvancedSpell, A2EventHeal):
    def __init__(self, time, parser):
        AEventAdvancedSpell.__init__(self, time, EventType.SPELL_PERIODIC_HEAL, parser)
        A2EventHeal.__init__(self, EventType.SPELL_PERIODIC_HEAL, parser)

    def encode(self, encoder: AEncoder) -> bytes:
        return AEventAdvancedSpell.encode(self, encoder) + A2EventHeal.encode(self, encoder)

    def __str__(self):
        return AEventAdvancedSpell.__str__(self) + A2EventHeal.__str__(self)

    def __eq__(self, other):
        return AEventAdvancedSpell.__eq__(other) and A2EventHeal.__eq__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

