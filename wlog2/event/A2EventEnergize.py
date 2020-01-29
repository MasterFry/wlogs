from abc import ABC

from ..types import EventType
from ..encode import AEncoder, ADecoder, SizeType

from ..EventParser import EventParser

# 36.0000,0.0000,0,8319
#  1:  amount
#  2:  overEnergize
#  3:  powerType
#  4:  alternatePowerType

class A2EventEnergize(ABC):
    def __init__(self, eventType, parser):
        assert(
            eventType == EventType.SPELL_ENERGIZE or \
            eventType == EventType.SPELL_PERIODIC_ENERGIZE
        )
        if isinstance(parser, EventParser):
            self.amount = parser.getFloat()
            self.overEnergize = parser.getFloat()
            self.powerType = parser.getInt()
            self.alternatePowerType = parser.getInt()
            
        elif isinstance(parser, ADecoder):
            self.decode(decode)
        else:
            ValueError('Parser not supported: ' + type(parser))

    def decode(self, decoder: ADecoder):
        self.amount = decoder.floating(size=SizeType.ENERGIZE_AMOUNT, digits=4)
        self.overEnergize = decoder.floating(size=SizeType.ENERGIZE_AMOUNT, digits=4)
        self.powerType = decoder.integer(size=SizeType.POWER_TYPE)
        self.alternatePowerType = decoder.integer(size=SizeType.ALTERNATE_POWER_TYPE)

    def encode(self, encoder: AEncoder) -> bytes:
        return encoder.floating(self.amount, size=SizeType.ENERGIZE_AMOUNT, digits=4) + \
               encoder.floating(self.overEnergize, size=SizeType.ENERGIZE_AMOUNT, digits=4) + \
               encoder.integer(self.powerType, size=SizeType.POWER_TYPE) + \
               encoder.integer(self.alternatePowerType, size=SizeType.ALTERNATE_POWER_TYPE)

    def __str__(self):
        return ',{0:.04f},{1:.04f},{2:d},{3:d}'.format(
            self.amount,
            self.overEnergize,
            self.powerType,
            self.alternatePowerType
        )

    def __eq__(self, other):
        return self.amount == other.amount             and \
               self.overEnergize == other.overEnergize and \
               self.powerType == other.powerType       and \
               self.alternatePowerType == other.alternatePowerType
        
    def __ne__(self, other):
        return not self.__eq__(other)

