
from ..types import EventType
from ..types import getAuraTypeName

from ..EventParser import EventParser

from .AEventBaseSpell import AEventBaseSpell

class EventSpellAuraBroken(AEventBaseSpell):
    def __init__(self, time, parser):
        AEventBaseSpell.__init__(self, time, EventType.SPELL_AURA_BROKEN, parser)
        
        if isinstance(parser, EventParser):
            self.auraType = parser.getAuraType()
            
        elif isinstance(parser, Decoder):
            self.decode(decode)
        else:
            ValueError('Parser not supported: ' + type(parser))

    def decode(self, decoder: Decoder):
        self.auraType = decoder.auraType()

    def encode(self, encoder: Encoder) -> bytes:
        return AEventBaseSpell.encode(self, encoder: Encoder) + encoder.auraType(self.auraType)

    def __str__(self):
        return AEventBaseSpell.__str__(self) + ',' + getAuraTypeName(self.auraType)

    def __eq__(self, other):
        return AEventBaseSpell.__eq__(other) and self.auraType == other.auraType
        
    def __ne__(self, other):
        return not self.__eq__(other)

