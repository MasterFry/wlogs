from .AEvent import string
from ..EventType import EventType
from .AEventBase import AEventBase
from .AEventAdvanced import AEventAdvanced
from ..EventParser import EventParser

class AEventAdvancedSpell(AEventAdvanced):
    def __init__(self, time, eventType, parser: EventParser):
        AEventBase.__init__(self, time, eventType, parser)

        # Prefix Parameters are inbetween Base and Advanced Parameters
        # e.g.: 11682,"Hellfire Effect",0x4
        self.spellId = parser.getInt()
        self.spellName = parser.getString()
        self.spellSchool = parser.getInt(base=16)
        
        AEventAdvanced.__init__(self, parser)

    def encode(self, encoder) -> bytes:
        return AEventBase.encode(self, encoder) + \
               encoder.spell(self.spellId, self.spellName, self.spellSchool) + \
               AEventAdvanced.encode(self, encoder)

    def __str__(self):
        return AEventBase.__str__(self) + ',{0:d},{1:s},{2:#x}'.format(
            self.spellId,
            string(self.spellName),
            self.spellSchool
        ) + AEventAdvanced.__str__(self)

    def __eq__(self, other):
        return AEventAdvanced.__eq__(other) and self.spellId == other.spellId

    def __ne__(self, other):
        return not self.__eq__(other)


