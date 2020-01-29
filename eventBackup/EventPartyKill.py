from ..EventType import EventType
from .AEventBase import AEventBase
from ..EventParser import EventParser

class EventPartyKill(AEventBase):
    def __init__(self, time, parser: EventParser):
        AEventBase.__init__(self, time, EventType.PARTY_KILL, parser)
