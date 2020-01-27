from abc import ABC

from ..EventType import EventType
from ..EventParser import EventParser

#  1:  amount
#  2:  overEnergize
#  3:  powerType
#  4:  alternatePowerType

class A2EventEnergize(ABC):
    def __init__(self, eventType, parser: EventParser):
        assert(
            eventType == EventType.SPELL_ENERGIZE or \
            eventType == EventType.SPELL_PERIODIC_ENERGIZE
        )
        self.amount = parser.getInt()
        self.overEnergize = parser.getInt()
        self.powerType = parser.getInt()
        self.alternatePowerType = parser.getInt()

    def __str__(self):
        return ',{0:d},{1:d},{2:d},{3:d}'.format(
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

