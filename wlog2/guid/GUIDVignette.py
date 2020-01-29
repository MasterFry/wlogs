from .AGUIDUnitType import AGUIDUnitType

from ..types import GUIDType
from ..EventParser import EventParser

class GUIDVignette(AGUIDUnitType):
    def __init__(self, parser: EventParser):
        AGUIDUnitType.__init__(self, GUIDType.VIGNETTE, parser)
    