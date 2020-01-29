from .AGUIDUnitType import AGUIDUnitType

from ..types import GUIDType

from ..EventParser import EventParser

class GUIDPet(AGUIDUnitType):
    def __init__(self, parser: EventParser):
        AGUIDUnitType.__init__(self, GUIDType.PET, parser)
    