
from ..types import EventType

from ..EventParser import EventParser

from .AEventAdvancedSpell import AEventAdvancedSpell

class EventSpellCastSuccess(AEventAdvancedSpell):
    def __init__(self, time, parser: EventParser):
        AEventAdvancedSpell.__init__(self, time, EventType.SPELL_CAST_SUCCESS, parser)
