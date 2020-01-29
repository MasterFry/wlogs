
from ..types import EventType

from ..EventParser import EventParser

from .AEventBase import AEventBase

class EventUnitLoyalty(AEventBase):
    def __init__(self, time, parser):
        AEventBase.__init__(self, time, EventType.UNIT_LOYALTY, parser)
