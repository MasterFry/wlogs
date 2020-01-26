from .Event import Event
from .EventType import EventType
from .EventAdvancedSpell import EventAdvancedSpell
from .EventParser import EventParser


class EventDamageShield(EventAdvancedSpell):
    def __init__(self, time, eventType, parser: EventParser):
        EventAdvancedSpell.__init__(self, time, eventType, parser)

    def getEventType(self) -> EventType:
        return EventType.DAMAGE_SHIELD

    def __str__(self):
        return EventAdvancedSpell.__str__(self)

    def __eq__(self, other):
        return EventAdvancedSpell.__eq__(other) and 

    def __ne__(self, other):
        return not self.__eq__(other)

