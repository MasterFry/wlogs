from ..types import GUIDType
from ..types import getGUIDTypeName

from ..EventParser import EventParser
from ..Encode import Encoder

from .AGUID import AGUID

class GUIDNull(AGUID):
    def __init__(self, parser: EventParser):
        AGUID.__init__(self, GUIDType.NULL)

    def encode(self, encoder):
        return encoder.guidType(self.guidType)

    def __str__(self):
        return getGUIDTypeName(self.guidType)
    