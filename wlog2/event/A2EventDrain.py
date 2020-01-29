from abc import ABC

from ..types import EventType

from ..Encode import SizeType
from ..EventParser import EventParser


# amount, powerType, extraAmount ?

class A2EventDrain(ABC):
    def __init__(self, eventType, parser: EventParser):
        assert(
            eventType == EventType.SPELL_DRAIN or \
            eventType == EventType.SPELL_PERIODIC_DRAIN or \
            eventType == EventType.SPELL_PERIODIC_LEECH
        )
        self.amount = parser.getInt()
        self.powerType = parser.getInt()
        self.extraAmount = parser.getInt()
        self.p6 = parser.getInt()

    def encode(self, encoder) -> bytes:
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

