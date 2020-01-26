from .Event import Event
from .EventType import EventType
from .EventParser import EventParser
from .EventEncounter import EventEncounter

# 1/22 19:39:52.829  ENCOUNTER_START,663,"Lucifron",9,40,409

class EventEncounterStart(EventEncounter):
    def __init__(self, time, parser: EventParser):
        EventEncounter.__init__(self, time, EventType.ENCOUNTER_START, parser)
        self.p6 = parser.getInt()

    def getEventType(self) -> EventType:
        return EventType.ENCOUNTER_START

    def __str__(self):
        return EventEncounter.__str__(self) + ',' + str(self.p6)

    def __eq__(self, other):
        return EventEncounter.__eq__(other) and \
               self.p6 == other.p6

    def __ne__(self, other):
        return not self.__eq__(other)