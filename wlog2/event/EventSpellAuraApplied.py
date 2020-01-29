
from ..types import EventType
from ..types import getAuraTypeName

from ..EventParser import EventParser

from .AEventSpellAura import AEventSpellAura

class EventSpellAuraApplied(AEventSpellAura):
    def __init__(self, time, parser: EventParser):
        AEventSpellAura.__init__(self, time, EventType.SPELL_AURA_APPLIED, parser)
