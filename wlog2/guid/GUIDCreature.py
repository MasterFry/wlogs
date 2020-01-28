from .AGUID import GUIDType
from .AGUIDUnitType import AGUIDUnitType

from ..EventParser import EventParser

class GUIDCreature(AGUIDUnitType):
    def __init__(self, parser: EventParser):
        AGUIDUnitType.__init__(self, GUIDType.CREATURE, parser)
    