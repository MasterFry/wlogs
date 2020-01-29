from ..EventType import EventType
from .AEventSpellAura import AEventSpellAura
from ..EventParser import EventParser
from ..AuraType import getAuraTypeName

class EventSpellAuraApplied(AEventSpellAura):
    def __init__(self, time, parser: EventParser):
        AEventSpellAura.__init__(self, time, EventType.SPELL_AURA_APPLIED, parser)
