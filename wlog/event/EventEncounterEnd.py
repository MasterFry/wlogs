from .Event import Event
from .EventType import EventType
from .EventParser import EventParser
from .EventEncounter import EventEncounter

# 1/22 19:39:52.829  ENCOUNTER_END,663,"Lucifron",9,40,1

class EventEncounterEnd(EventEncounter):
    def __init__(self, time, parser: EventParser):
        EventEncounter.__init__(self, time, EventType.ENCOUNTER_END, parser)
        self.success = True if parser.readValue() == '1' else False

    def getEventType(self) -> EventType:
        return EventType.ENCOUNTER_END

    def __str__(self):
        return EventEncounter.__str__(self) + (',1' if self.success else ',0')

    def __eq__(self, other):
        return EventEncounter.__eq__(other) and \
               self.success == other.success

    def __ne__(self, other):
        return not self.__eq__(other)