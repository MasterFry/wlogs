from .AEvent import string
from ..EventType import EventType
from .AEventBaseSpell import AEventBaseSpell
from ..EventParser import EventParser
from ..AuraType import getAuraTypeName

class EventSpellAuraBrokenSpell(AEventBaseSpell):
    def __init__(self, time, parser: EventParser):
        AEventBaseSpell.__init__(self, time, EventType.SPELL_AURA_BROKEN_SPELL, parser)
        self.extraSpellId = parser.getInt()
        self.extraSpellName = parser.getString()
        self.extraSpellSchool = parser.getInt()
        self.auraType = parser.getAuraType()

    def encode(self, encoder) -> bytes:
        return AEventBaseSpell.encode(encoder) + \
               encoder.spell(self.extraSpellId, self.extraSpellName, self.extraSpellSchool) + \
               encoder.auraType(self.auraType)

    def __str__(self):
        return AEventBaseSpell.__str__(self) + ',{0:d},{1:s},{2:d},{3:s}'.format(
            self.extraSpellId,
            string(self.extraSpellName),
            self.extraSpellSchool,
            getAuraTypeName(self.auraType)
        )

    def __eq__(self, other):
        return AEventBaseSpell.__eq__(other) and \
               self.extraSpellId == other.extraSpellId and \
               self.auraType == other.auraType
        
    def __ne__(self, other):
        return not self.__eq__(other)

