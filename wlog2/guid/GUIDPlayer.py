from ..types import GUIDType
from ..types import getGUIDTypeName
from ..encode import AEncoder, ADecoder, SizeType

from ..EventParser import EventParser

from .AGUID import AGUID

# For players: Player-[server ID]-[player UID] (Example: "Player-970-0002FD64")

class GUIDPlayer(AGUID):
    def __init__(self, parser):
        AGUID.__init__(self, GUIDType.PLAYER)
        
        if isinstance(parser, EventParser):
            self.serverID = parser.getInt(delim='-')
            self.playerUID = parser.getInt(delim=',', base=16)
            
        elif isinstance(parser, ADecoder):
            self.decode(decode)
        else:
            ValueError('Parser not supported: ' + type(parser))

    def decode(self, decoder: ADecoder):
        self.serverID = self.integer(size=SizeType.GUID_SERVER_ID)
        self.playerUID = self.integer(size=SizeType.GUID_PLAYER_UID)

    def encode(self, encoder: AEncoder):
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
    