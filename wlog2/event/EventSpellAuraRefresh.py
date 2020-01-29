
from ..types import EventType
from ..types import getAuraTypeName

from ..EventParser import EventParser

from .AEventSpellAura import AEventSpellAura

class EventSpellAuraRefresh(AEventSpellAura):
    def __init__(self, time, parser):
        AEventSpellAura.__init__(self, time, EventType.SPELL_AURA_REFRESH, parser)
