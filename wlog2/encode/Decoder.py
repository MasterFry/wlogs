from ..Time import Time

from ..types import *
from ..guid import *
from ..event import *

from .SizeType import SizeType
from .ADecoder import ADecoder

class Decoder(ADecoder):
    def __init__(self, fname: str):
        ADecoder.__init__(self, fname)

    def guid(self):
        gType = self.guidType()
        return GUID_TABLE[gType](self)

    def event(self):
        eTime = self.time()
        eType = self.eventType()
        return EVENT_TABLE[eType](eTime, self)

    def time(self):
        return Time(self)

    def __enter__(self):
        self.open(self.fname)
        return self

    def __exit__(self, ex_type, ex_value, ex_traceback):
        if ex_type is not None:
            raise
        self.close()
