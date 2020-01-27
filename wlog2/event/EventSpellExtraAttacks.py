from ..EventType import EventType
from .AEventBaseSpell import AEventBaseSpell
from ..EventParser import EventParser

class EventSpellExtraAttacks(AEventBaseSpell):
    def __init__(self, time, parser: EventParser):
        AEventBaseSpell.__init__(self, time, EventType.SPELL_EXTRA_ATTACKS, parser)
        self.amount = parser.getInt()

    def encode(self, encoder) -> bytes:
        return AEventBaseSpell.encode(encoder) + encoder.integer(self.amount, size=1)

    def __str__(self):
        return AEventBaseSpell.__str__(self) + ',{0:d}'.format(
            self.amount
        )

    def __eq__(self, other):
        return AEventBaseSpell.__eq__(other) and self.amount == other.amount
        
    def __ne__(self, other):
        return not self.__eq__(other)

