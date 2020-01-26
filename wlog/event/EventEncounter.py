from .Event import Event
from .EventType import EventType
from .EventParser import EventParser

# 1/22 19:39:52.829  ENCOUNTER_START,663,"Lucifron",9,40,409
# 1/22 19:39:52.829  ENCOUNTER_END,663,"Lucifron",9,40,1

class EventEncounter(Event):
    def __init__(self, time, eventType, parser: EventParser):
        Event.__init__(self, time, eventType)
        self.encounterId = parser.getInt()
        self.encounterName = parser.getString()
        self.difficultyId = parser.getInt()
        self.playerCount = parser.getInt()

    def __str__(self):
        return Event.__str__(self) + ',{0:d},"{1:s}",{2:d},{3:d}'.format(
            self.encounterId,
            self.encounterName,
            self.difficultyId,
            self.playerCount
        )

    def __eq__(self, other):
        return Event.__eq__(other) and \
               self.encounterId == other.encounterId and \
               self.difficultyId == other.difficultyId and \
               self.playerCount == other.playerCount

    def __ne__(self, other):
        return not self.__eq__(other)