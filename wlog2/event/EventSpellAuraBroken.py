
from ..types import EventType
from ..types import getAuraTypeName
from ..encode.AEncoder import AEncoder
from ..encode.ADecoder import ADecoder

from ..EventParser import EventParser

from .AEventBaseSpell import AEventBaseSpell

class EventSpellAuraBroken(AEventBaseSpell):
    def __init__(self, time, parser):
        AEventBaseSpell.__init__(self, time, EventType.SPELL_AURA_BROKEN, parser)
        
        if isinstance(parser, EventParser):
            self.auraType = parser.getAuraType()
            
        elif isinstance(parser, ADecoder):
            self.decode(decode)
        else:
            ValueError('Parser not supported: ' + type(parser))

    def decode(self, decoder: ADecoder):
        self.auraType = decoder.auraType()

    def encode(self, encoder: AEncoder) -> bytes:
        return AEventBaseSpell.encode(self, encoder) + encoder.auraType(self.auraType)

    def __str__(self):
        return AEventBaseSpell.__str__(self) + ',' + getAuraTypeName(self.auraType)

    def __eq__(self, other):
        return AEventBaseSpell.__eq__(self, other) and self.auraType == other.auraType
        
    def __ne__(self, other):
        return not self.__eq__(other)

