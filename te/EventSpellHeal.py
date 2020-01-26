from .Event import Event
from .EventType import EventType
from .EventBase import EventBase
from .EventAdvanced import EventAdvanced
from .EventParser import EventParser

class EventSpellHeal(EventAdvanced):
    def __init__(self, time, parser: EventParser):
        EventBase.__init__(self, time)
        EventAdvanced.__init__(self, time)

    def getEventType(self) -> EventType:
        return EventType.SPELL_HEAL

    def __str__(self):
        return EventBase.__str__(self) + EventAdvanced.__str__(self)

    def __eq__(self, other):
        return EventAdvanced.__eq__(other) and 
    def __ne__(self, other):
        return not self.__eq__(other)

