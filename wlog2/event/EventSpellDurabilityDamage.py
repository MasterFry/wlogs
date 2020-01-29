
from ..types import EventType

from ..EventParser import EventParser

from .AEvent import string
from .AEventBaseSpell import AEventBaseSpell

class EventSpellDurabilityDamage(AEventBaseSpell):
    def __init__(self, time, parser):
        AEventBaseSpell.__init__(self, time, EventType.SPELL_DURABILITY_DAMAGE, parser)
        
        if isinstance(parser, EventParser):
            self.itemId = parser.getInt()
            self.itemName = parser.getString()
            
        elif isinstance(parser, ADecoder):
            self.decode(decode)
        else:
            ValueError('Parser not supported: ' + type(parser))

    def decode(self, decoder: ADecoder):
        self.itemId, self.itemName = decoder.item()

    def encode(self, encoder: AEncoder) -> bytes:
        return AEventBaseSpell.encode(self, encoder: AEncoder) + encoder.item(self.itemId, self.itemName)

    def __str__(self):
        return AEventBaseSpell.__str__(self) + ',{0:d},{1:s}'.format(
            self.itemId,
            string(self.itemName)
        )

    def __eq__(self, other):
        return AEventBaseSpell.__eq__(other) and self.itemId == other.itemId
        
    def __ne__(self, other):
        return not self.__eq__(other)

