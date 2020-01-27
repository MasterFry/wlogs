from abc import ABC

from ..EventType import EventType
from ..EventParser import EventParser

# amount, powerType, extraAmount ?

class A2EventDrain(ABC):
    def __init__(self, eventType, parser: EventParser):
        assert(
            eventType == EventType.SPELL_DRAIN or \
            eventType == EventType.SPELL_PERIODIC_DRAIN or \
            eventType == EventType.SPELL_PERIODIC_LEECH
        )
        assert(parser.getInt() == 50)
        assert(parser.getInt() == 4)
        assert(parser.getInt() == 0)
        assert(parser.getInt() == 1000000)

    def encode(self, encoder) -> bytes:
        return b''

    def __str__(self):
        return ',50,4,0,1000000'

    def __eq__(self, other):
        return True
        
    def __ne__(self, other):
        return not self.__eq__(other)

