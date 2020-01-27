from abc import ABC

from ..EventType import EventType
from ..EventParser import EventParser

# 296,296,0,0,nil
# 1224,1224,1224,0,nil
#  1:  amount
#  2:  overhealing
#  3:  absorbed
#  4:  ?
#  5:  critical: nil / 1

class A2EventHeal(ABC):
    def __init__(self, eventType, parser: EventParser):
        assert(
            eventType == EventType.SPELL_HEAL or \
            eventType == EventType.SPELL_PERIODIC_HEAL
        )
        self.amount = parser.getInt()
        self.overhealing = parser.getInt()
        self.absorbed = parser.getInt()
        self.p1 = parser.getInt()
        self.critical = parser.readValue() == '1'

    def encode(self, encoder) -> bytes:
        return encoder.floating(self.amount, size=2, digits=4) + \
               encoder.floating(self.overEnergize, size=2, digits=4) + \
               encoder.integer(self.powerType, size=1) + \
               encoder.integer(self.p1, size=1) + \
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

