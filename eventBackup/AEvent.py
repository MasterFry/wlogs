from abc import ABC
from abc import abstractmethod

from wlog import Time
from ..EventType import EventType
from ..EventType import getEventName
from ..Encode import Encoder

# Unknown Parameters:
# A2EventHeal: p1
# A2EventDamage: p2, p3
# EventEncounterStart: p4
# EventSpellAbsorbed: p5

def string(s: str):
    return 'nil' if s is None else '"' + s + '"'


class AEvent(ABC):
    def __init__(self, time, eventType):
        self.time = time
        self.eventType = eventType

    def getEventName(self) -> str:
        return getEventName(self.eventType)

    def encode(self, encoder) -> bytes:
        return encoder.time(self.time) + encoder.eventType(self.eventType)

    def __str__(self):
        return str(self.time) + '  ' + self.getEventName()

    def __eq__(self, other):
        return self.eventType == other.eventType

    def __ne__(self, other):
        return self.eventType != other.eventType