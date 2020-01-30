from ..types import GUIDType
from ..types import getGUIDTypeName
from ..encode.AEncoder import AEncoder
from ..encode.ADecoder import ADecoder

from ..EventParser import EventParser

from .AGUID import AGUID

class GUIDNull(AGUID):
    def __init__(self, parser):
        AGUID.__init__(self, GUIDType.NULL)

    def decode(self, decoder: ADecoder):
        pass

    def encode(self, encoder):
        return encoder.guidType(self.guidType)

    def __str__(self):
        return getGUIDTypeName(self.guidType)
    