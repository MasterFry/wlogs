from ..EventType import EventType
from .AEventBaseSpell import AEventBaseSpell
from .A2EventMissed import A2EventMissed
from ..EventParser import EventParser

class EventSpellPeriodicMissed(AEventBaseSpell, A2EventMissed):
    def __init__(self, time, eventType, parser: EventParser):
        AEventBaseSpell.__init__(self, time, EventType.SPELL_MISSED, parser)
        A2EventMissed.__init__(self, EventType.SPELL_MISSED, parser)

    def __str__(self):
        return AEventBaseSpell.__str__(self) + A2EventMissed.__str__(self)

    def __eq__(self, other):
        return AEventBaseSpell.__eq__(self) and A2EventMissed.__eq__(self)
        
    def __ne__(self, other):
        return not self.__eq__(other)