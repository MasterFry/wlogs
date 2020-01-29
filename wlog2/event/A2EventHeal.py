from abc import ABC

from ..types import EventType
from ..encode import *

from ..EventParser import EventParser

# 296,296,0,0,nil
# 1224,1224,1224,0,nil
#  1:  amount
#  2:  overhealing
#  3:  absorbed
#  4:  ?
#  5:  critical: nil / 1

class A2EventHeal(ABC):
    def __init__(self, eventType, parser):
        assert(
            eventType == EventType.SPELL_HEAL or \
            eventType == EventType.SPELL_PERIODIC_HEAL
        )
        if isinstance(parser, EventParser):
            self.amount = parser.getInt()
            self.overhealing = parser.getInt()
            self.absorbed = parser.getInt()
            self.p1 = parser.getInt()
            self.critical = parser.readValue() == '1'
            
        elif isinstance(parser, Decoder):
            self.decode(decode)
        else:
            ValueError('Parser not supported: ' + type(parser))

    def decode(self, decoder: Decoder):
        self.amount = decoder.integer(size, size=SizeType.HEAL_AMOUNT)
        self.overhealing = decoder.integer(size, size=SizeType.HEAL_AMOUNT)
        self.absorbed = decoder.integer(size, size=SizeType.HEAL_AMOUNT)
        self.p1 = decoder.integer(size, size=SizeType.HEAL_P1)
        self.critical = decoder.boolean()

    def encode(self, encoder: Encoder) -> bytes:
        return encoder.integer(self.amount, size=SizeType.HEAL_AMOUNT) + \
               encoder.integer(self.overhealing, size=SizeType.HEAL_AMOUNT) + \
               encoder.integer(self.absorbed, size=SizeType.HEAL_AMOUNT) + \
               encoder.integer(self.p1, size=SizeType.HEAL_P1) + \
               encoder.boolean(self.critical)


    def __str__(self):
        return ',{0:d},{1:d},{2:d},{3:d},{4:s}'.format(
            self.amount,
            self.overhealing,
            self.absorbed,
            self.p1,
            '1' if self.critical else 'nil'
        )

    def __eq__(self, other):
        return self.amount == other.amount           and \
               self.overhealing == other.overhealing and \
               self.absorbed == other.absorbed       and \
               self.p1 == other.p1                   and \
               self.critical == other.critical
        
    def __ne__(self, other):
        return not self.__eq__(other)

