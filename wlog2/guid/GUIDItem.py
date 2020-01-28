from .AGUID import GUIDType
from .AGUID import AGUID

from ..EventParser import EventParser

# For items: Item-[server ID]-0-[spawn UID] (Example: "Item-970-0-400000076620BFF4")
#   (Please note that this tells you nothing useful about the item, like the ID)

class GUIDItem(AGUID):
    def __init__(self, parser: EventParser):
        AGUID.__init__(self, GUIDType.ITEM)
        self.serverID = parser.getInt(delim='-')
        assert(parser.readValue(delim='-') == '0')
        self.spawnUID = parser.getInt(delim=',', base=16)

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
    