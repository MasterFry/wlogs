from .Event import Event
from .EventType import EventType
from .EventBase import EventBase
from .EventAdvanced import EventAdvanced
from .EventParser import EventParser

class EventAdvancedSpell(EventAdvanced):
    def __init__(self, time, eventType, parser: EventParser):
        EventBase.__init__(self, time, eventType, parser)

        # Prefix Parameters are inbetween Base and Advanced Parameters
        # e.g.: 11682,"Hellfire Effect",0x4
        self.spellId = parser.getInt()
        self.spellName = parser.getString()
        self.spellSchool = parser.getInt(base=16)
        
        EventAdvanced.__init__(self, parser)

    def __str__(self):
        return EventBase.__str__(self) + ',{0:d},"{1:s}",{2:#x}'.format(
            self.spellId,
            self.spellName,
            self.spellSchool
        ) + EventAdvanced.__str__(self)

    def __eq__(self, other):
        return EventAdvanced.__eq__(other) and self.spellId == other.spellId

    def __ne__(self, other):
        return not self.__eq__(other)


