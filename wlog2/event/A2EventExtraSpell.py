from abc import ABC

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
        self.extraSpellSchool = parser.getInt(base=16)

    def __str__(self):
        return AEventBaseSpell.__str__(self) + ',{0:d},"{1:s}",{2:#x}'.format(
            self.extraSpellId,
            self.extraSpellName,
            self.extraSpellSchool
        )

    def __eq__(self, other):
        return self.extraSpellId == other.extraSpellId
        
    def __ne__(self, other):
        return not self.__eq__(other)

