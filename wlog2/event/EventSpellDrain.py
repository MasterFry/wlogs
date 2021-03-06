
from ..types import EventType
from ..encode.AEncoder import AEncoder

from ..EventParser import EventParser

from .A2EventDrain import A2EventDrain
from .AEventAdvancedSpell import AEventAdvancedSpell

class EventSpellDrain(AEventAdvancedSpell, A2EventDrain):
    def __init__(self, time, parser):
        AEventAdvancedSpell.__init__(self, time, EventType.SPELL_DRAIN, parser)
        A2EventDrain.__init__(self, EventType.SPELL_DRAIN, parser)

    def encode(self, encoder: AEncoder) -> bytes:
        return AEventAdvancedSpell.encode(self, encoder) + A2EventDrain.encode(self, encoder)

    def __str__(self):
        return AEventAdvancedSpell.__str__(self) + A2EventDrain.__str__(self)

    def __eq__(self, other):
        return AEventAdvancedSpell.__eq__(self, other) and A2EventDrain.__eq__(self, other)
        
    def __ne__(self, other):
        return not self.__eq__(other)

