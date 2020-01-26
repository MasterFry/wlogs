from .Event import Event
from .EventType import EventType
from .EventBaseSpell import EventBaseSpell
from .EventParser import EventParser

class EventSpellSummon(EventBaseSpell):
    def __init__(self, time, eventType, parser: EventParser):
        EventBaseSpell.__init__(self, time, eventType, parser)

    def getEventType(self) -> EventType:
        return EventType.SPELL_SUMMON

    def __str__(self):
        return EventBaseSpell.__str__(self) +

    def __eq__(self, other):
        return EventBaseSpell.__eq__(other) and 
        
    def __ne__(self, other):
        return not self.__eq__(other)

