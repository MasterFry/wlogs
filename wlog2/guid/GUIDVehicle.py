from .AGUID import GUIDType
from .AGUIDUnitType import AGUIDUnitType

from ..EventParser import EventParser

class GUIDVehicle(AGUIDUnitType):
    def __init__(self, parser: EventParser):
        AGUIDUnitType.__init__(self, GUIDType.VEHICLE, parser)
    