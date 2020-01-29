from ..EventType import EventType
from ..EventParser import EventParser
from .AEventEncounter import AEventEncounter
from ..Encode import SizeType

# 1/22 19:39:52.829  ENCOUNTER_START,663,"Lucifron",9,40,409

class EventEncounterStart(AEventEncounter):
    def __init__(self, time, parser: EventParser):
        AEventEncounter.__init__(self, time, EventType.ENCOUNTER_START, parser)
        self.p4 = parser.getInt()

    def encode(self, encoder) -> bytes:
        return AEventEncounter.encode(encoder) + encoder.integer(self.p4, size=SizeType.ENCOUNTER_START_P4)

    def getEventType(self) -> EventType:
        return EventType.ENCOUNTER_START

    def __str__(self):
        return AEventEncounter.__str__(self) + ',' + str(self.p4)

    def __eq__(self, other):
        return AEventEncounter.__eq__(other) and \
               self.p4 == other.p4

    def __ne__(self, other):
        return not self.__eq__(other)