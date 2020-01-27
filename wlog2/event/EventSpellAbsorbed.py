from ..EventType import EventType
from .AEventBaseSpell import AEventBaseSpell
from ..EventParser import EventParser

class EventSpellAbsorbed(AEventBaseSpell):
    def __init__(self, time, parser: EventParser):
        AEventBaseSpell.__init__(self, time, EventType.SPELL_ABSORBED, parser)
        self.amount = parser.getInt()

    def __str__(self):
        return AEventBaseSpell.__str__(self) + ',{0:d}'.format(
            self.amount
        )

    def __eq__(self, other):
        return AEventBaseSpell.__eq__(other) and self.amount == other.amount

    def __ne__(self, other):
        return not self.__eq__(other)
