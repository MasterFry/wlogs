from ..EventType import EventType
from .AEventBaseSpell import AEventBaseSpell
from ..EventParser import EventParser

class EventSpellDurabilityDamage(AEventBaseSpell):
    def __init__(self, time, parser: EventParser):
        AEventBaseSpell.__init__(self, time, EventType.SPELL_DURABILITY_DAMAGE, parser)
        self.itemId = parser.getInt()
        self.itemName = parser.getString()

    def __str__(self):
        return AEventBaseSpell.__str__(self) + ',{0:d},"{1:s}"'.format(
            self.itemId,
            self.itemName
        )

    def __eq__(self, other):
        return AEventBaseSpell.__eq__(other) and self.itemId == other.itemId
        
    def __ne__(self, other):
        return not self.__eq__(other)

