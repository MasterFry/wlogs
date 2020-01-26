from .Event import Event
from .EventType import EventType
from .EventParser import EventParser

# 

class Event(Event):
    def __init__(self, time, parser: EventParser):
        Event.__init__(time)

    def getEventType(self) -> EventType:
        return EventType.

    def __str__(self):
        return Event.__str__(self) +

    def __eq__(self, other):
        return Event.__eq__(other) and \

    def __ne__(self, other):
        return not self.__eq__(other)