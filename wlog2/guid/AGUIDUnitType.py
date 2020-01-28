from .AGUID import GUIDType
from .AGUID import getGUIDTypeName
from .AGUID import AGUID

from ..EventParser import EventParser

# For Unit Type Names: [Unit type]-0-[server ID]-[instance ID]-[zone UID]-[ID]-[spawn UID] 
#   Unit Type Names: "Creature", "Pet", "GameObject", "Vehicle", and "Vignette"
#   (Example: "Creature-0-970-0-11-31146-000136DF91")

class AGUIDUnitType(AGUID):
    def __init__(self, guidType: GUIDType, parser: EventParser):
        AGUID.__init__(self, guidType)
        assert(parser.readValue(delim='-') == '0')
        self.serverID = parser.getInt(delim='-')
        self.instanceID = parser.getInt(delim='-')
        self.zoneUID = parser.getInt(delim='-')
        self.ID = parser.getInt(delim='-')
        self.spawnUID = parser.getInt(delim=',', base=16)

    def __str__(self):
        return '{0:s}-0-{1:d}-{2:d}-{3:d}-{4:d}-{5:010X}'.format(
            getGUIDTypeName(self.guidType),
            self.serverID,
            self.instanceID,
            self.zoneUID,
            self.ID,
            self.spawnUID
        )

    def __eq__(self, other):
        return AGUID.__eq__(self, other) and \
               self.serverID == other.serverID and \
               self.instanceID == other.instanceID and \
               self.zoneUID == other.zoneUID and \
               self.ID == other.ID and \
               self.spawnUID == other.spawnUID

    def __ne__(self, other):
        return not self.__eq__(other)
    