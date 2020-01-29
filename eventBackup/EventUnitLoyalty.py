from ..EventType import EventType
from .AEventBase import AEventBase
from ..EventParser import EventParser

class EventUnitLoyalty(AEventBase):
    def __init__(self, time, parser: EventParser):
        AEventBase.__init__(self, time, EventType.UNIT_LOYALTY, parser)
