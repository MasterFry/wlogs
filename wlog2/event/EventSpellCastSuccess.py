from ..EventType import EventType
from .AEventAdvancedSpell import AEventAdvancedSpell
from ..EventParser import EventParser

class EventSpellCastSuccess(AEventAdvancedSpell):
    def __init__(self, time, parser: EventParser):
        AEventAdvancedSpell.__init__(self, time, EventType.SPELL_CAST_SUCCESS, parser)

    def __str__(self):
        return AEventBase.__str__(self) + AEventAdvancedSpell.__str__(self)

    def __eq__(self, other):
        return AEventAdvancedSpell.__eq__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

