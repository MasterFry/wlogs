from ..EventType import EventType
from .AEventBase import AEventBase
from .AEventAdvanced import AEventAdvanced
from ..EventParser import EventParser

class EventSwingDamageLanded(AEventAdvanced):
    def __init__(self, time, parser: EventParser):
        assert(False and "Not implemented yet!")
        AEventBase.__init__(self, time, EventType.SWING_DAMAGE_LANDED, parser)
        AEventAdvanced.__init__(self, parser)

    def __str__(self):
        return AEventBase.__str__(self) + AEventAdvanced.__str__(self)

    def __eq__(self, other):
        return AEventAdvanced.__eq__(other)
        
    def __ne__(self, other):
        return not self.__eq__(other)

