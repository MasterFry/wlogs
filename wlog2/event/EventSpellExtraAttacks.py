
from ..types import EventType
from ..encode.AEncoder import AEncoder
from ..encode.ADecoder import ADecoder
from ..encode.SizeType import SizeType

from ..EventParser import EventParser

from .AEventBaseSpell import AEventBaseSpell

class EventSpellExtraAttacks(AEventBaseSpell):
    def __init__(self, time, parser):
        AEventBaseSpell.__init__(self, time, EventType.SPELL_EXTRA_ATTACKS, parser)
        
        if isinstance(parser, EventParser):
            self.amount = parser.getInt()
            
        elif isinstance(parser, ADecoder):
            self.decode(decode)
        else:
            ValueError('Parser not supported: ' + type(parser))

    def decode(self, decoder: ADecoder):
        self.amount = decoder.integer(size=SizeType.EXTRA_ATTACK_AMOUNT)

    def encode(self, encoder: AEncoder) -> bytes:
        return AEventBaseSpell.encode(self, encoder) + encoder.integer(self.amount, size=SizeType.EXTRA_ATTACK_AMOUNT)

    def __str__(self):
        return AEventBaseSpell.__str__(self) + ',{0:d}'.format(
            self.amount
        )

    def __eq__(self, other):
        return AEventBaseSpell.__eq__(self, other) and self.amount == other.amount
        
    def __ne__(self, other):
        return not self.__eq__(other)

