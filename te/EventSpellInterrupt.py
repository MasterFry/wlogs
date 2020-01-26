from .Event import Event
from .EventType import EventType
from .EventBase import EventBase
from .EventParser import EventParser

class EventEventSpellInterrupt(EventBase):
    def __init__(self, time, parser: EventParser):
        EventBase.__init__(self, time)

    def getEventType(self) -> EventType:
        return EventType.SPELL_INTERRUPT

    def __str__(self):
        return EventBase.__str__(self) +

    def __eq__(self, other):
        return EventBase.__eq__(other) and 
    def __ne__(self, other):
        return not self.__eq__(other)

