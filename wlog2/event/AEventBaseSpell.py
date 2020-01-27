from .AEvent import string
from ..EventType import EventType
from .AEventBase import AEventBase
from ..EventParser import EventParser

class AEventBaseSpell(AEventBase):
    def __init__(self, time, eventType, parser: EventParser):
        AEventBase.__init__(self, time, eventType, parser)
        self.spellId = parser.getInt()
        self.spellName = parser.getString()
        self.spellSchool = parser.getInt(base=16)

    def __str__(self):
        return AEventBase.__str__(self) + ',{0:d},{1:s},{2:#x}'.format(
            self.spellId,
            string(self.spellName),
            self.spellSchool
        )

    def __eq__(self, other):
        return AEventBase.__eq__(other) and self.spellId == other.spellId

    def __ne__(self, other):
        return not self.__eq__(other)

