from ..event import *

from .AEncoder import AEncoder

class Encoder(AEncoder):
    def __init__(self):
        pass

    def event(self, event) -> bytes:
        return event.encode(self)
