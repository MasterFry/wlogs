from .Event import Event
from .EventType import EventType
from .EventBase import EventBase
from .EventAdvanced import EventAdvanced
from .EventParser import EventParser

class EventEnvironmentalDamage(EventAdvanced):
    def __init__(self, time, eventType, parser: EventParser):
        EventBase.__init__(self, time, eventType, parser)
        EventAdvanced.__init__(self, parser)

    def getEventType(self) -> EventType:
        return EventType.ENVIRONMENTAL_DAMAGE

    def __str__(self):
        return EventBase.__str__(self) + EventAdvanced.__str__(self)

    def __eq__(self, other):
        return EventAdvanced.__eq__(other) and 
        
    def __ne__(self, other):
        return not self.__eq__(other)

