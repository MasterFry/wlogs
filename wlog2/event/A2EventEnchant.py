from abc import ABC

from ..types import EventType

from ..EventParser import EventParser

from .AEvent import string

#  1:  spellName
#  2:  itemId
#  3:  itemName

class A2EventEnchant(ABC):
    def __init__(self, eventType, parser):
        assert(
            eventType == EventType.ENCHANT_APPLIED or \
            eventType == EventType.ENCHANT_REMOVED
        )
        raise ValueError("Entry for confirmation required")
        if isinstance(parser, EventParser):
            self.spellName = parser.getString()
            self.itemId = parser.getInt()
            self.itemName = parser.getString()
            
        elif isinstance(parser, Decoder):
            self.decode(decode)
        else:
            ValueError('Parser not supported: ' + type(parser))

    def decode(self, decoder: Decoder):
        self.spellName = decoder.string()
        self.itemId, self.itemName = decoder.item()

    def encode(self, encoder: Encoder) -> bytes:
        return encoder.string(self.spellName) + encoder.item(self.itemId, self.itemName)

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
