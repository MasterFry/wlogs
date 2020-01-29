from ..EventType import EventType
from .AEventAdvancedSpell import AEventAdvancedSpell
from ..EventParser import EventParser

class EventSpellCastSuccess(AEventAdvancedSpell):
    def __init__(self, time, parser: EventParser):
        AEventAdvancedSpell.__init__(self, time, EventType.SPELL_CAST_SUCCESS, parser)
