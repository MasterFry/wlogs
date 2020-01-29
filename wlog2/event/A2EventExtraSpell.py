from abc import ABC

from ..types import EventType

from ..EventParser import EventParser

from .AEvent import string

class A2EventExtraSpell(ABC):
    def __init__(self, eventType, parser):
        assert(
            eventType == EventType.SPELL_DISPEL or \
            eventType == EventType.SPELL_INTERRUPT
        )
        if isinstance(parser, EventParser):
            self.extraSpellId = parser.getInt()
            self.extraSpellName = parser.getString()
            self.extraSpellSchool = parser.getInt()
            
        elif isinstance(parser, Decoder):
            self.decode(decode)
        else:
            ValueError('Parser not supported: ' + type(parser))

    def decode(self, decoder: Decoder):
        self.extraSpellName, self.extraSpellId, self.extraSpellName = decoder.spell()

    def encode(self, encoder: Encoder) -> bytes:
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

