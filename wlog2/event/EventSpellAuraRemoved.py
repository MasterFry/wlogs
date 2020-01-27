from ..EventType import EventType
from .AEventSpellAura import AEventSpellAura
from ..EventParser import EventParser
from ..AuraType import getAuraTypeName

class EventSpellAuraRemoved(AEventSpellAura):
    def __init__(self, time, parser: EventParser):
        AEventSpellAura.__init__(self, time, EventType.SPELL_AURA_REMOVED, parser)

    def __str__(self):
        return AEventSpellAura.__str__(self)

    def __eq__(self, other):
        return AEventSpellAura.__eq__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

