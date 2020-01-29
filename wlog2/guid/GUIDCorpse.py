from .AGUIDUnitType import AGUIDUnitType

from ..types import GUIDType

from ..EventParser import EventParser

class GUIDCorpse(AGUIDUnitType):
    def __init__(self, parser: EventParser):
        AGUIDUnitType.__init__(self, GUIDType.CORPSE, parser)
        assert(False and 'Sample required!')
    