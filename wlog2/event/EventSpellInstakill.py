
from ..types import EventType

from ..EventParser import EventParser

from .AEventBaseSpell import AEventBaseSpell

class EventSpellInstakill(AEventBaseSpell):
    def __init__(self, time, parser: EventParser):
        AEventBaseSpell.__init__(self, time, EventType.SPELL_INSTAKILL, parser)
