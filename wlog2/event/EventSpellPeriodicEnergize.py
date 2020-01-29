
from ..types import EventType

from ..EventParser import EventParser

from .A2EventEnergize import A2EventEnergize
from .AEventAdvancedSpell import AEventAdvancedSpell

class EventSpellPeriodicEnergize(AEventAdvancedSpell):
    def __init__(self, time, parser: EventParser):
        AEventAdvancedSpell.__init__(self, time, EventType.SPELL_PERIODIC_ENERGIZE, parser)
        A2EventEnergize.__init__(self, EventType.SPELL_PERIODIC_ENERGIZE, parser)

    def encode(self, encoder) -> bytes:
        return AEventAdvancedSpell.encode(self, encoder) + A2EventEnergize.encode(self, encoder)
        
    def __str__(self):
        return AEventAdvancedSpell.__str__(self) + A2EventEnergize.__str__(self)

    def __eq__(self, other):
        return AEventAdvancedSpell.__eq__(other) and A2EventEnergize.__eq__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

