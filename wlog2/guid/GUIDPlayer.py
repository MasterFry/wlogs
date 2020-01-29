from ..types import GUIDType
from ..types import getGUIDTypeName

from ..EventParser import EventParser
from ..Encode import Encoder
from ..Encode import SizeType

from .AGUID import AGUID

# For players: Player-[server ID]-[player UID] (Example: "Player-970-0002FD64")

class GUIDPlayer(AGUID):
    def __init__(self, parser: EventParser):
        AGUID.__init__(self, GUIDType.PLAYER)
        self.serverID = parser.getInt(delim='-')
        self.playerUID = parser.getInt(delim=',', base=16)

    def encode(self, encoder: Encoder):
        return encoder.guidType(self.guidType) + \
               encoder.integer(self.serverID, size=SizeType.GUID_SERVER_ID) + \
               encoder.integer(self.playerUID, size=SizeType.GUID_PLAYER_UID)

    def __str__(self):
        return 'Player-{0:d}-{1:08X}'.format(
            self.serverID,
            self.playerUID
        )

    def __eq__(self, other):
        return AGUID.__eq__(self, other) and \
               self.serverID == other.serverID and \
               self.playerUID == other.playerUID

    def __ne__(self, other):
        return not self.__eq__(other)
    