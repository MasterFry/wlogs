from abc import ABC

from ..types import EventType
from ..encode.AEncoder import AEncoder
from ..encode.ADecoder import ADecoder
from ..encode.SizeType import SizeType

from ..EventParser import EventParser


# amount, powerType, extraAmount ?

class A2EventDrain(ABC):
    def __init__(self, eventType, parser):
        assert(
            eventType == EventType.SPELL_DRAIN or \
            eventType == EventType.SPELL_PERIODIC_DRAIN or \
            eventType == EventType.SPELL_PERIODIC_LEECH
        )
        if isinstance(parser, EventParser):
            self.amount = parser.getInt()
            self.powerType = parser.getInt()
            self.extraAmount = parser.getInt()
            self.p6 = parser.getInt()
            
        elif isinstance(parser, ADecoder):
            self.decode(decode)
        else:
            ValueError('Parser not supported: ' + type(parser))

    def decode(self, decoder: ADecoder):
        self.amount = decoder.integer(size=SizeType.DRAIN_AMOUNT)
        self.powerType = decoder.integer(size=SizeType.POWER_TYPE)
        self.extraAmount = decoder.integer(size=SizeType.DRAIN_AMOUNT)
        self.p6 = decoder.integer(size=SizeType.DRAIN_P6)

    def encode(self, encoder: AEncoder) -> bytes:
        return encoder.integer(self.amount, size=SizeType.DRAIN_AMOUNT) + \
               encoder.integer(self.powerType, size=SizeType.POWER_TYPE) + \
               encoder.integer(self.extraAmount, size=SizeType.DRAIN_AMOUNT) + \
               encoder.integer(self.p6, size=SizeType.DRAIN_P6)

    def __str__(self):
        return ',{0:d},{1:d},{2:d},{3:d}'.format(
            self.amount,
            self.powerType,
            self.extraAmount,
            self.p6
        )

    def __eq__(self, other):
        return self.amount == other.amount and \
               self.powerType == other.powerType and \
               self.extraAmount == other.extraAmount and \
               self.p6 == other.p6
        
    def __ne__(self, other):
        return not self.__eq__(other)

