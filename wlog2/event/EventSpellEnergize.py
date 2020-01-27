from ..EventType import EventType
from .AEventAdvancedSpell import AEventAdvancedSpell
from .A2EventEnergize import A2EventEnergize
from ..EventParser import EventParser

class EventSpellEnergize(AEventAdvancedSpell, A2EventEnergize):
    def __init__(self, time, parser: EventParser):
        AEventAdvancedSpell.__init__(self, time, EventType.SPELL_ENERGIZE, parser)
        A2EventEnergize.__init__(self, EventType.SPELL_ENERGIZE, parser)
        
    def __str__(self):
        return AEventAdvancedSpell.__str__(self) + A2EventEnergize.__str__(self)

    def __eq__(self, other):
        return AEventAdvancedSpell.__eq__(other) and A2EventEnergize.__eq__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

