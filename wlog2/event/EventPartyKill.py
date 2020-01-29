
from ..types import EventType

from ..EventParser import EventParser

from .AEventBase import AEventBase

class EventPartyKill(AEventBase):
    def __init__(self, time, parser):
        AEventBase.__init__(self, time, EventType.PARTY_KILL, parser)
