from abc import ABC

from .AEvent import string
from ..EventType import EventType
from ..EventParser import EventParser

class A2EventExtraSpell(ABC):
    def __init__(self, eventType, parser: EventParser):
        assert(
            eventType == EventType.SPELL_DISPEL or \
            eventType == EventType.SPELL_INTERRUPT
        )
        self.extraSpellId = parser.getInt()
        self.extraSpellName = parser.getString()
        self.extraSpellSchool = parser.getInt()

    def encode(self, encoder) -> bytes:
        return encoder.spell(self.extraSpellId, self.extraSpellName, self.extraSpellSchool)

    def __str__(self):
        return ',{0:d},{1:s},{2:d}'.format(
            self.extraSpellId,
            string(self.extraSpellName),
            self.extraSpellSchool
        )

    def __eq__(self, other):
        return self.extraSpellId == other.extraSpellId
        
    def __ne__(self, other):
        return not self.__eq__(other)

