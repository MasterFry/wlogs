from ..EventType import EventType
from .AEventBaseSpell import AEventBaseSpell
from ..EventParser import EventParser

class EventSpellCastFailed(AEventBaseSpell):
    def __init__(self, time, parser: EventParser):
        AEventBaseSpell.__init__(self, time, EventType.SPELL_CAST_FAILED, parser)
        self.failedType = parser.getString()

    def encode(self, encoder) -> bytes:
        return AEventBaseSpell.encode(encoder) + encoder.string(self.failedType)

    def __str__(self):
        return AEventBaseSpell.__str__(self) + ',"{0:s}"'.format(
            self.failedType
        )

    def __eq__(self, other):
        return AEventBaseSpell.__eq__(other)
        
    def __ne__(self, other):
        return not self.__eq__(other)
