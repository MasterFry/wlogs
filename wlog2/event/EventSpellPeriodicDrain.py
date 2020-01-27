from ..EventType import EventType
from .AEventAdvancedSpell import AEventAdvancedSpell
from .A2EventDrain import A2EventDrain
from ..EventParser import EventParser

class EventSpellPeriodicDrain(AEventAdvancedSpell, A2EventDrain):
    def __init__(self, time, parser: EventParser):
        AEventAdvancedSpell.__init__(self, time, EventType.SPELL_PERIODIC_DRAIN, parser)
        A2EventDrain.__init__(self, EventType.SPELL_PERIODIC_DRAIN, parser)

    def __str__(self):
        return AEventAdvancedSpell.__str__(self) + A2EventDrain.__str__(self)

    def __eq__(self, other):
        return AEventAdvancedSpell.__eq__(other) and A2EventDrain.__eq__(other)
        
    def __ne__(self, other):
        return not self.__eq__(other)

