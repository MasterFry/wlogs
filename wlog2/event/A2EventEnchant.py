from abc import ABC

from .AEvent import string
from ..EventType import EventType
from ..EventParser import EventParser

#  1:  spellName
#  2:  itemId
#  3:  itemName

class A2EventEnchant(ABC):
    def __init__(self, eventType, parser: EventParser):
        assert(
            eventType == EventType.ENCHANT_APPLIED or \
            eventType == EventType.ENCHANT_REMOVED
        )
        self.spellName = parser.getString()
        self.itemId = parser.getInt()
        self.itemName = parser.getString()
        assert(False and "Entry for confirmation required")

    def __str__(self):
        return ',{0:s},{1:d},{2:s}'.format(
            string(self.spellName),
            self.itemId,
            string(self.itemName)
        )

    def __eq__(self, other):
        return self.spellName == other.spellName and \
               self.itemId == other.itemId       and \
               self.itemName == other.itemName
        
    def __ne__(self, other):
        return not self.__eq__(other)

