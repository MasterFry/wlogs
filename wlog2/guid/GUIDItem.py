from ..types import GUIDType
from ..types import getGUIDTypeName
from ..encode import AEncoder, ADecoder, SizeType

from ..EventParser import EventParser

from .AGUID import AGUID

# For items: Item-[server ID]-0-[spawn UID] (Example: "Item-970-0-400000076620BFF4")
#   (Please note that this tells you nothing useful about the item, like the ID)

class GUIDItem(AGUID):
    def __init__(self, parser):
        AGUID.__init__(self, GUIDType.ITEM)
        
        if isinstance(parser, EventParser):
            self.serverID = parser.getInt(delim='-')
            assert(parser.readValue(delim='-') == '0')
            self.spawnUID = parser.getInt(delim=',', base=16)
            
        elif isinstance(parser, ADecoder):
            self.decode(decode)
        else:
            ValueError('Parser not supported: ' + type(parser))

    def decode(self, decoder: ADecoder):
        self.serverID = self.integer(size=SizeType.GUID_SERVER_ID)
        self.spawnUID = self.integer(size=SizeType.GUID_ITEM_SPAWN_UID)

    def encode(self, encoder: AEncoder):
        return encoder.guidType(self.guidType) + \
               encoder.integer(self.serverID, size=SizeType.GUID_SERVER_ID) + \
               encoder.integer(self.spawnUID, size=SizeType.GUID_ITEM_SPAWN_UID)

    def __str__(self):
        return 'Item-{0:d}-0-{1:016X}'.format(
            self.serverID,
            self.spawnUID
        )

    def __eq__(self, other):
        return AGUID.__eq__(self, other) and \
               self.serverID == other.serverID and \
               self.spawnUID == other.spawnUID

    def __ne__(self, other):
        return not self.__eq__(other)
    