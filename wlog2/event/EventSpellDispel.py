
from ..types import EventType
from ..types import getAuraTypeName
from ..encode.AEncoder import AEncoder
from ..encode.ADecoder import ADecoder

from ..EventParser import EventParser

from .A2EventExtraSpell import A2EventExtraSpell
from .AEventBaseSpell import AEventBaseSpell

class EventSpellDispel(AEventBaseSpell, A2EventExtraSpell):
    def __init__(self, time, parser):
        AEventBaseSpell.__init__(self, time, EventType.SPELL_DISPEL, parser)
        A2EventExtraSpell.__init__(self, EventType.SPELL_DISPEL, parser)
        
        if isinstance(parser, EventParser):
            self.auraType = parser.getAuraType()
            
        elif isinstance(parser, ADecoder):
            self.decode(decode)
        else:
            ValueError('Parser not supported: ' + type(parser))

    def decode(self, decoder: ADecoder):
        self.auraType = decoder.auraType()

    def encode(self, encoder: AEncoder) -> bytes:
        return AEventBaseSpell.encode(self, encoder) + \
               A2EventExtraSpell.encode(self, encoder) + \
               encoder.auraType(self.auraType)

    def __str__(self):
        return AEventBaseSpell.__str__(self) + A2EventExtraSpell.__str__(self) + ',{0:s}'.format(
            getAuraTypeName(self.auraType)
        )

    def __eq__(self, other):
        return AEventBaseSpell.__eq__(self, other) and \
               A2EventExtraSpell.__eq__(self, other)    and \
               self.auraType == other.auraType
        
    def __ne__(self, other):
        return not self.__eq__(other)

