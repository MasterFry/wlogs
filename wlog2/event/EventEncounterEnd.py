
from ..types import EventType

from ..EventParser import EventParser

from .AEventEncounter import AEventEncounter

# 1/22 19:39:52.829  ENCOUNTER_END,663,"Lucifron",9,40,1

class EventEncounterEnd(AEventEncounter):
    def __init__(self, time, parser: EventParser):
        AEventEncounter.__init__(self, time, EventType.ENCOUNTER_END, parser)
        self.success = True if parser.readValue() == '1' else False

    def encode(self, encoder) -> bytes:
        return AEventEncounter.encode(self, encoder) + encoder.boolean(self.success)

    def getEventType(self) -> EventType:
        return EventType.ENCOUNTER_END

    def __str__(self):
        return AEventEncounter.__str__(self) + (',1' if self.success else ',0')

    def __eq__(self, other):
        return AEventEncounter.__eq__(other) and \
               self.success == other.success

    def __ne__(self, other):
        return not self.__eq__(other)