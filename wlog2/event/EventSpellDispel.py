from ..EventType import EventType
from .AEventBaseSpell import AEventBaseSpell
from .A2EventExtraSpell import A2EventExtraSpell
from ..EventParser import EventParser
from ..AuraType import getAuraTypeName

class EventSpellDispel(AEventBaseSpell, A2EventExtraSpell):
    def __init__(self, time, parser: EventParser):
        AEventBaseSpell.__init__(self, time, EventType.SPELL_DISPEL, parser)
        A2EventExtraSpell.__init__(self, EventType.SPELL_DISPEL, parser)
        self.auraType = parser.getAuraType()

    def __str__(self):
        return AEventBaseSpell.__str__(self) + A2EventExtraSpell.__str__(self) + ',{0:s}'.format(
            getAuraTypeName(self.auraType)
        )

    def __eq__(self, other):
        return AEventBaseSpell.__eq__(other) and \
               A2EventExtraSpell.__eq__(other)    and \
               self.auraType == other.auraType
        
    def __ne__(self, other):
        return not self.__eq__(other)

