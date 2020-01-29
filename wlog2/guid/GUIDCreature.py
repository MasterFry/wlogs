from .AGUIDUnitType import AGUIDUnitType

from ..types import GUIDType

from ..EventParser import EventParser

class GUIDCreature(AGUIDUnitType):
    def __init__(self, parser):
        AGUIDUnitType.__init__(self, GUIDType.CREATURE, parser)
    