from .AGUID import GUIDType
from .AGUID import getGUIDTypeName
from .AGUID import AGUID

from ..EventParser import EventParser

class GUIDNull(AGUID):
    def __init__(self, parser: EventParser):
        AGUID.__init__(self, GUIDType.NULL)

    def __str__(self):
        return getGUIDTypeName(self.guidType)
    