from enum import Enum

# For players: Player-[server ID]-[player UID] (Example: "Player-970-0002FD64")
# For creatures, pets, objects, and vehicles: [Unit type]-0-[server ID]-[instance ID]-[zone UID]-[ID]-[spawn UID] (Example: "Creature-0-970-0-11-31146-000136DF91")
#   Unit Type Names: "Creature", "Pet", "GameObject", "Vehicle", and "Vignette"
# For items: Item-[server ID]-0-[spawn UID] (Example: "Item-970-0-400000076620BFF4") (Please note that this tells you nothing useful about the item, like the ID)
class GUID:
    def __init__(self, guid: str):
        r = guid.split('-')

        # Check GUID Type
        if len(r) == 1 and int(r[0]) == 0:
            self.type = GUID.TYPE.NULL
        elif r[0] == 'Player':
            self.type = GUID.TYPE.PLAYER
        elif r[0] == 'Creature':
            self.type = GUID.TYPE.CREATURE
        elif r[0] == 'Pet':
            self.type = GUID.TYPE.PET
        elif r[0] == 'GameObject':
            self.type = GUID.TYPE.GAME_OBJECT
        elif r[0] == 'Vehicle':
            self.type = GUID.TYPE.VEHICLE
        elif r[0] == 'Vignette':
            self.type = GUID.TYPE.VIGNETTE
        elif r[0] == 'Item':
            self.type = GUID.TYPE.ITEM
        elif r[0] == 'Corpse':
            # Corpse-0-4445-409-24916-0-0000067792
            self.type = GUID.TYPE.CORPSE
        else:
            raise ValueError('Invalid GUID Type: ' + guid)
        
        # Read GUID IDs
        if self.type == GUID.TYPE.PLAYER:
            assert(len(r) == 3)
            assert(len(r[2]) == 8)
            self.serverID   = int(r[1], 16)
            self.playerUID  = int(r[2], 16)
        elif self.type == GUID.TYPE.ITEM:
            assert(len(r) == 4)
            assert(r[2] == '0')
            assert(len(r[3]) == 16)
            self.serverID   = int(r[1], 16)
            self.spawnUID   = int(r[3], 16)
        elif self.type != GUID.TYPE.NULL:
            assert(len(r) == 7)
            assert(r[1] == '0')
            assert(len(r[6]) == 10)
            self.serverID   = int(r[2], 16)
            self.instanceID = int(r[3], 16)
            self.zoneUID    = int(r[4], 16)
            self.ID         = int(r[5], 16)
            self.spawnUID   = int(r[6], 16)
        else:
            if self.type != GUID.TYPE.NULL:
                print(self.type)
                assert(False and 'GUID has no or invalid Type?')

    def __str__(self):
        if self.type == GUID.TYPE.NULL:
            return '0000000000000000'
        if self.type == GUID.TYPE.PLAYER:
            return 'Player-%X-%08X' % (self.serverID, self.playerUID)
        if self.type == GUID.TYPE.CREATURE:
            return 'Creature-0-%X-%X-%X-%X-%010X' % (self.serverID, self.instanceID, self.zoneUID, self.ID, self.spawnUID)
        if self.type == GUID.TYPE.PET:
            return 'Pet-0-%X-%X-%X-%X-%010X' % (self.serverID, self.instanceID, self.zoneUID, self.ID, self.spawnUID)
        if self.type == GUID.TYPE.GAME_OBJECT:
            return 'GameObject-0-%X-%X-%X-%X-%010X' % (self.serverID, self.instanceID, self.zoneUID, self.ID, self.spawnUID)
        if self.type == GUID.TYPE.VEHICLE:
            return 'Vehicle-0-%X-%X-%X-%X-%010X' % (self.serverID, self.instanceID, self.zoneUID, self.ID, self.spawnUID)
        if self.type == GUID.TYPE.VIGNETTE:
            return 'Vignette-0-%X-%X-%X-%X-%010X' % (self.serverID, self.instanceID, self.zoneUID, self.ID, self.spawnUID)
        if self.type == GUID.TYPE.CORPSE:
            return 'Corpse-0-%X-%X-%X-%X-%010X' % (self.serverID, self.instanceID, self.zoneUID, self.ID, self.spawnUID)
        if self.type == GUID.TYPE.ITEM:
            return 'Item-%X-0-%016X' % (self.serverID, self.spawnUID)
        print(self.type)
        assert(False and 'GUID has no or invalid Type?')

    def __eq__(self, other):
        if not isinstance(other, GUID):
            return False
        if self.type != other.type:
            return False
        if self.type == GUID.TYPE.NULL:
            return True
        if self.serverID != other.serverID:
            return False
        if self.type == GUID.TYPE.PLAYER:
            return self.playerUID == other.playerUID
        if self.type == GUID.TYPE.ITEM:
            return self.spawnUID == other.spawnUID
        return self.instanceID == other.instanceID and \
               self.zoneUID == other.zoneUID and \
               self.ID == other.ID and \
               self.spawnUID == other.spawnUID
    
    def __ne__(self, other):
        return not self.__eq__(other)

    class TYPE(Enum):
        NULL = 0
        PLAYER = 1
        CREATURE = 2
        PET = 3
        GAME_OBJECT = 4
        VEHICLE = 5
        VIGNETTE = 6
        ITEM = 7
        CORPSE = 8