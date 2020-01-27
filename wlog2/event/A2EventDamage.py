from abc import ABC

from ..EventType import EventType
from ..EventParser import EventParser

# 986,896,-1,16,0,0,0,nil,nil,nil
#  1:  amount:
#  2:  ?: 0 - 5000
#  3:  ?: -1 - 2579
#  4:  school: 0 - 127
#  5:  resisted:
#  6:  blocked:
#  7:  absorbed:
#  8:  critical: nil / 1
#  9:  glancing: nil / 1
# 10:  crushing: nil / 1

class A2EventDamage(ABC):
    def __init__(self, eventType, parser: EventParser):
        assert(
            eventType == EventType.ENVIRONMENTAL_DAMAGE  or \
            eventType == EventType.RANGE_DAMAGE          or \
            eventType == EventType.SPELL_DAMAGE          or \
            eventType == EventType.SPELL_PERIODIC_DAMAGE or \
            eventType == EventType.SWING_DAMAGE          or \
            eventType == EventType.SWING_DAMAGE_LANDED   or \
            eventType == EventType.DAMAGE_SHIELD
        )
        self.amount = parser.getInt()
        self.p2 = parser.getInt()
        self.p3 = parser.getInt()
        self.school = parser.getInt()
        self.resisted = parser.getInt()
        self.blocked = parser.getInt()
        self.absorbed = parser.getInt()
        self.critical = parser.readValue() == '1'
        self.glancing = parser.readValue() == '1'
        self.crushing = parser.readValue() == '1'

    def __str__(self):
        return ',{0:d},{1:d},{2:d},{3:d},{4:d},{5:d},{6:d},{7:s},{8:s},{9:s}'.format(
            self.amount,
            self.p2,
            self.p3,
            self.school,
            self.resisted,
            self.blocked,
            self.absorbed,
            '1' if self.critical else 'nil',
            '1' if self.glancing else 'nil',
            '1' if self.crushing else 'nil'
        )

    def __eq__(self, other):
        return self.amount == other.amount     and \
               self.p2 == other.p2             and \
               self.p3 == other.p3             and \
               self.school == other.school     and \
               self.resisted == other.resisted and \
               self.blocked == other.blocked   and \
               self.absorbed == other.absorbed and \
               self.critical == other.critical and \
               self.glancing == other.glancing and \
               self.crushing == other.crushing
        
    def __ne__(self, other):
        return not self.__eq__(other)

