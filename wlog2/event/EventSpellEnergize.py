
from ..types import EventType
from ..encode.AEncoder import AEncoder

from ..EventParser import EventParser

from .A2EventEnergize import A2EventEnergize
from .AEventAdvancedSpell import AEventAdvancedSpell

class EventSpellEnergize(AEventAdvancedSpell, A2EventEnergize):
    def __init__(self, time, parser):
        AEventAdvancedSpell.__init__(self, time, EventType.SPELL_ENERGIZE, parser)
        A2EventEnergize.__init__(self, EventType.SPELL_ENERGIZE, parser)

    def encode(self, encoder: AEncoder) -> bytes:
        return AEventAdvancedSpell.encode(self, encoder) + A2EventEnergize.encode(self, encoder)
        
    def __str__(self):
        return AEventAdvancedSpell.__str__(self) + A2EventEnergize.__str__(self)

    def __eq__(self, other):
        return AEventAdvancedSpell.__eq__(self, other) and A2EventEnergize.__eq__(self, other)

    def __ne__(self, other):
        return not self.__eq__(other)

