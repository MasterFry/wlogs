from ..EventType import EventType
from .AEventBaseSpell import AEventBaseSpell
from ..EventParser import EventParser
from ..AuraType import getAuraTypeName

class EventSpellAuraBroken(AEventBaseSpell):
    def __init__(self, time, parser: EventParser):
        AEventBaseSpell.__init__(self, time, EventType.SPELL_AURA_BROKEN, parser)
        self.auraType = parser.getAuraType()

    def __str__(self):
        return AEventBaseSpell.__str__(self) + ',' + getAuraTypeName(self.auraType)

    def __eq__(self, other):
        return AEventBaseSpell.__eq__(other) and self.auraType == other.auraType
        
    def __ne__(self, other):
        return not self.__eq__(other)

