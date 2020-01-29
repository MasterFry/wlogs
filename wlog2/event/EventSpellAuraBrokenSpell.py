
from ..types import EventType
from ..types import getAuraTypeName

from ..EventParser import EventParser

from .AEvent import string
from .AEventBaseSpell import AEventBaseSpell

class EventSpellAuraBrokenSpell(AEventBaseSpell):
    def __init__(self, time, parser):
        AEventBaseSpell.__init__(self, time, EventType.SPELL_AURA_BROKEN_SPELL, parser)
        
        if isinstance(parser, EventParser):
            self.extraSpellId = parser.getInt()
            self.extraSpellName = parser.getString()
            self.extraSpellSchool = parser.getInt()
            self.auraType = parser.getAuraType()
            
        elif isinstance(parser, ADecoder):
            self.decode(decode)
        else:
            ValueError('Parser not supported: ' + type(parser))

    def decode(self, decoder: ADecoder):
        self.extraSpellId, self.extraSpellName, self.extraSpellSchool = decoder.spell()
        self.auraType = decoder.auraType()

    def encode(self, encoder: AEncoder) -> bytes:
        return AEventBaseSpell.encode(self, encoder: AEncoder) + \
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

