from ..EventType import EventType
from .AEventBaseSpell import AEventBaseSpell
from ..EventParser import EventParser

class EventSpellCastStart(AEventBaseSpell):
    def __init__(self, time, parser: EventParser):
        AEventBaseSpell.__init__(self, time, EventType.SPELL_CAST_START, parser)

    def encode(self, encoder) -> bytes:
        return AEventBaseSpell.encode(encoder)

    def __str__(self):
        return AEventBaseSpell.__str__(self)

    def __eq__(self, other):
        return AEventBaseSpell.__eq__(other)
        
    def __ne__(self, other):
        return not self.__eq__(other)

