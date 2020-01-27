from ..EventType import EventType
from .AEventBaseSpell import AEventBaseSpell
from ..EventParser import EventParser
from ..AuraType import getAuraTypeName

class AEventSpellAura(AEventBaseSpell):
    def __init__(self, time, eventType, parser: EventParser):
        assert(
            eventType == EventType.SPELL_AURA_APPLIED or \
            eventType == EventType.SPELL_AURA_REMOVED or \
            eventType == EventType.SPELL_AURA_APPLIED_DOSE or \
            eventType == EventType.SPELL_AURA_REMOVED_DOSE or \
            eventType == EventType.SPELL_AURA_REFRESH
        )
        AEventBaseSpell.__init__(self, time, eventType, parser)
        self.auraType = parser.getAuraType()
        self.amount = parser.getInt()

    def __str__(self):
        return AEventBaseSpell.__str__(self) + ',{0:s},{1:d}'.format(
            getAuraTypeName(self.auraType),
            self.amount
        )

    def __eq__(self, other):
        return AEventBaseSpell.__eq__(other) and \
               self.auraType == other.auraType and \
               self.amount == other.amount

    def __ne__(self, other):
        return not self.__eq__(other)

