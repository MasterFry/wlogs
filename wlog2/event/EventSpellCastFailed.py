
from ..types import EventType

from ..EventParser import EventParser

from .AEventBaseSpell import AEventBaseSpell

class EventSpellCastFailed(AEventBaseSpell):
    def __init__(self, time, parser: EventParser):
        AEventBaseSpell.__init__(self, time, EventType.SPELL_CAST_FAILED, parser)
        self.failedType = parser.getString()

    def encode(self, encoder) -> bytes:
        return AEventBaseSpell.encode(self, encoder) + encoder.string(self.failedType)

    def __str__(self):
        return AEventBaseSpell.__str__(self) + ',"{0:s}"'.format(
            self.failedType
        )

    def __eq__(self, other):
        return AEventBaseSpell.__eq__(other)
        
    def __ne__(self, other):
        return not self.__eq__(other)

