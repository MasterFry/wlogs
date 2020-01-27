from abc import ABC

from ..EventType import EventType
from ..EventParser import EventParser

#  1:  amount
#  2:  overhealing
#  3:  absorbed
#  4:  critical: nil / 1

class A2EventHeal(ABC):
    def __init__(self, eventType, parser: EventParser):
        assert(
            eventType == EventType.SPELL_HEAL or \
            eventType == EventType.SPELL_PERIODIC_HEAL
        )
        self.amount = parser.getInt()
        self.overhealing = parser.getInt()
        self.absorbed = parser.getInt()
        self.critical = parser.readValue() == '1'

    def __str__(self):
        return ',{0:d},{1:d},{2:d},{3:s}'.format(
            self.amount,
            self.overhealing,
            self.absorbed,
            '1' if self.critical else 'nil'
        )

    def __eq__(self, other):
        return self.amount == other.amount           and \
               self.overhealing == other.overhealing and \
               self.absorbed == other.absorbed       and \
               self.critical == other.critical
        
    def __ne__(self, other):
        return not self.__eq__(other)

