from abc import ABC
from abc import abstractmethod

from .EventType import EventType
from .EventType import EVENT_NAMES

class Event(ABC):
    def __init__(self, time):
        self.time = time
    
    @abstractmethod
    def getEventType(self) -> EventType:
        pass

    def getEventName(self) -> str:
        return EVENT_NAMES[int(self.getEventType())]

    def __str__(self):
        return str(self.time) + '  ' + self.getEventName()

    def __eq__(self, other):
        return self.getEventType() == other.getEventType()

    def __ne__(self, other):
        return self.getEventType() != other.getEventType()

# COMBAT_LOG_VERSION
# COMBATANT_INFO
# ENCOUNTER_START
# ENCOUNTER_END