from .AGUIDUnitType import AGUIDUnitType

from ..types import GUIDType
from ..encode.AEncoder import AEncoder
from ..encode.ADecoder import ADecoder
from ..encode.SizeType import SizeType

from ..EventParser import EventParser

class GUIDCorpse(AGUIDUnitType):
    def __init__(self, parser):
        AGUIDUnitType.__init__(self, GUIDType.CORPSE, parser)
    