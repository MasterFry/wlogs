from .Event import Event
from .EventType import EventType
from .EventBase import EventBase
from .EventParser import EventParser

class EventEventSpellInstakill(EventBase):
    def __init__(self, time, parser: EventParser):
        EventBase.__init__(self, time)

        # Prefix Parameters are inbetween Base and Advanced Parameters
        # e.g.: 11682,"Hellfire Effect",0x4
        self.spellId = parser.getInt()
        self.spellName = parser.getString()
        self.spellSchool = parser.getInt(base=16)
        

    def getEventType(self) -> EventType:
        return EventType.SPELL_INSTAKILL

    def __str__(self):
        return EventBase.__str__(self) +

    def __eq__(self, other):
        return EventBase.__eq__(other) and 
    def __ne__(self, other):
        return not self.__eq__(other)

