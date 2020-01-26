from .Event import Event
from .EventType import EventType
from .EventBase import EventBase
from .EventParser import EventParser

class EventUnitDied(EventBase):
    def __init__(self, time, eventType, parser: EventParser):
        EventBase.__init__(self, time, eventType, parser)

    def getEventType(self) -> EventType:
        return EventType.UNIT_DIED

    def __str__(self):
        return EventBase.__str__(self) +

    def __eq__(self, other):
        return EventBase.__eq__(other) and 
        
    def __ne__(self, other):
        return not self.__eq__(other)

