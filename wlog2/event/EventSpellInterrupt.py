
from ..types import EventType

from ..EventParser import EventParser

from .A2EventExtraSpell import A2EventExtraSpell
from .AEventBaseSpell import AEventBaseSpell

class EventSpellInterrupt(AEventBaseSpell, A2EventExtraSpell):
    def __init__(self, time, parser):
        AEventBaseSpell.__init__(self, time, EventType.SPELL_INTERRUPT, parser)
        A2EventExtraSpell.__init__(self, EventType.SPELL_INTERRUPT, parser)

    def encode(self, encoder: Encoder) -> bytes:
        return AEventBaseSpell.encode(self, encoder: Encoder) + A2EventExtraSpell.encode(self, encoder: Encoder)

    def __str__(self):
        return AEventBaseSpell.__str__(self) + A2EventExtraSpell.__str__(self)

    def __eq__(self, other):
        return AEventBaseSpell.__eq__(other) and A2EventExtraSpell.__eq__(other)
        
    def __ne__(self, other):
        return not self.__eq__(other)

