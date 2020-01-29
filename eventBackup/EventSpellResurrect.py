from ..EventType import EventType
from .AEventBaseSpell import AEventBaseSpell
from ..EventParser import EventParser

class EventSpellResurrect(AEventBaseSpell):
    def __init__(self, time, parser: EventParser):
        AEventBaseSpell.__init__(self, time, EventType.SPELL_RESURRECT, parser)
