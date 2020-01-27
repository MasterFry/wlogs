from abc import ABC

from ..EventType import EventType
from ..EventParser import EventParser
from ..MissType import MissType
from ..MissType import getMissTypeName

class A2EventMissed(ABC):
    def __init__(self, eventType, parser: EventParser):
        assert(
            eventType == EventType.SWING_MISSED or \
            eventType == EventType.RANGE_MISSED or \
            eventType == EventType.SPELL_MISSED or \
            eventType == EventType.SPELL_PERIODIC_MISSED
        )
        self.missType = parser.getMissType()
        self.isOffHand = parser.readValue() == '1'

        if self.missType == MissType.ABSORB:
            self.amountMissed = parser.getInt()
            self.critical = parser.getInt()

        elif self.missType == MissType.RESIST or \
             self.missType == MissType.BLOCK:
            self.amountMissed = parser.getInt()

    def __str__(self):
        if self.missType == MissType.ABSORB:
            return ',{0:s},{1:s},{2:d},{3:d}'.format(
                getMissTypeName(self.missType),
                '1' if self.isOffHand else 'nil',
                self.amountMissed,
                self.critical
            )
        elif self.missType == MissType.RESIST or \
             self.missType == MissType.BLOCK:
            return ',{0:s},{1:s},{2:d}'.format(
                getMissTypeName(self.missType),
                '1' if self.isOffHand else 'nil',
                self.amountMissed
            )
        else:
            return ',{0:s},{1:s}'.format(
                getMissTypeName(self.missType),
                '1' if self.isOffHand else 'nil'
            )

    def __eq__(self, other):
        if self.missType != other.missType:
            return False

        if self.missType == MissType.ABSORB:
            return self.amountMissed == other.amountMissed and \
                   self.critical == other.critical

        elif self.missType == MissType.RESIST or \
             self.missType == MissType.BLOCK:
            return self.amountMissed == other.amountMissed

        return True
        
    def __ne__(self, other):
        return not self.__eq__(other)

