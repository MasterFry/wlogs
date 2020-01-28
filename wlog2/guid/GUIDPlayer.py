from .AGUID import GUIDType
from .AGUID import AGUID

from ..EventParser import EventParser

# For players: Player-[server ID]-[player UID] (Example: "Player-970-0002FD64")

class GUIDPlayer(AGUID):
    def __init__(self, parser: EventParser):
        AGUID.__init__(self, GUIDType.PLAYER)
        self.serverID = parser.getInt(delim='-')
        self.playerUID = parser.getInt(delim=',', base=16)

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
    