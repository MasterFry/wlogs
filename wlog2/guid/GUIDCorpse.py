from .AGUIDUnitType import AGUIDUnitType

from ..types import GUIDType
from ..encode import AEncoder, ADecoder, SizeType

from ..EventParser import EventParser

class GUIDCorpse(AGUIDUnitType):
    def __init__(self, parser):
        AGUIDUnitType.__init__(self, GUIDType.CORPSE, parser)
        assert(False and 'Sample required!')
    