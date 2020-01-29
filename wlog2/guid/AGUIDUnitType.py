from ..types import GUIDType
from ..types import getGUIDTypeName
from ..encode import AEncoder, ADecoder, SizeType

from ..EventParser import EventParser

from .AGUID import AGUID

# For Unit Type Names: [Unit type]-0-[server ID]-[instance ID]-[zone UID]-[ID]-[spawn UID] 
#   Unit Type Names: "Creature", "Pet", "GameObject", "Vehicle", and "Vignette"
#   (Example: "Creature-0-970-0-11-31146-000136DF91")

class AGUIDUnitType(AGUID):
    def __init__(self, guidType: GUIDType, parser):
        AGUID.__init__(self, guidType)
        
        if isinstance(parser, EventParser):
            assert(parser.readValue(delim='-') == '0')
            self.serverID = parser.getInt(delim='-')
            self.instanceID = parser.getInt(delim='-')
            self.zoneUID = parser.getInt(delim='-')
            self.ID = parser.getInt(delim='-')
            self.spawnUID = parser.getInt(delim=',', base=16)
            
        elif isinstance(parser, ADecoder):
            self.decode(decode)
        else:
            ValueError('Parser not supported: ' + type(parser))

    def decode(self, decoder: ADecoder):
        self.serverID = self.integer(size=SizeType.GUID_SERVER_ID)
        self.instanceID = self.integer(size=SizeType.GUID_INSTANCE_ID)
        self.zoneUID = self.integer(size=SizeType.GUID_ZONE_UID)
        self.ID = self.integer(size=SizeType.GUID_ID)
        self.spawnUID = self.integer(size=SizeType.GUID_SPAWN_UID)

    def encode(self, encoder: AEncoder):
        return encoder.guidType(self.guidType) + \
               encoder.integer(self.serverID, size=SizeType.GUID_SERVER_ID) + \
               encoder.integer(self.instanceID, size=SizeType.GUID_INSTANCE_ID) + \
               encoder.integer(self.zoneUID, size=SizeType.GUID_ZONE_UID) + \
               encoder.integer(self.ID, size=SizeType.GUID_ID) + \
               encoder.integer(self.spawnUID, size=SizeType.GUID_SPAWN_UID)

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
    