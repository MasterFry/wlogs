from ..EventType import EventType
from .AEventBase import AEventBase
from ..EventParser import EventParser

class EventPartyKill(AEventBase):
    def __init__(self, time, parser: EventParser):
        AEventBase.__init__(self, time, EventType.PARTY_KILL, parser)

    def __str__(self):
        return AEventBase.__str__(self)

    def __eq__(self, other):
        return AEventBase.__eq__(other)
        
    def __ne__(self, other):
        return not self.__eq__(other)

