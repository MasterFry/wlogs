# Type
COMBATLOG_OBJECT_TYPE_MASK            = 0x0000FC00
COMBATLOG_OBJECT_TYPE_PET             = 0x00001000
COMBATLOG_OBJECT_TYPE_PLAYER          = 0x00000400

# Controller Afiiliation
COMBATLOG_OBJECT_AFFILIATION_MASK     = 0x0000000F
COMBATLOG_OBJECT_AFFILIATION_OUTSIDER = 0x00000008
COMBATLOG_OBJECT_AFFILIATION_RAID     = 0x00000004
COMBATLOG_OBJECT_AFFILIATION_PARTY    = 0x00000002
COMBATLOG_OBJECT_AFFILIATION_MINE     = 0x00000001

class UnitFlag:
    # Type
    @staticmethod
    def isPet(flag):
        return (flag & COMBATLOG_OBJECT_TYPE_MASK) == COMBATLOG_OBJECT_TYPE_PET
    @staticmethod
    def isPlayer(flag):
        return (flag & COMBATLOG_OBJECT_TYPE_MASK) == COMBATLOG_OBJECT_TYPE_PLAYER
    # Controller Afiiliation
    @staticmethod
    def isOutsider(flag):
        return (flag & COMBATLOG_OBJECT_AFFILIATION_MASK) == COMBATLOG_OBJECT_AFFILIATION_OUTSIDER
    @staticmethod
    def isRaid(flag):
        return (flag & COMBATLOG_OBJECT_AFFILIATION_MASK) == COMBATLOG_OBJECT_AFFILIATION_RAID
    @staticmethod
    def isParty(flag):
        return (flag & COMBATLOG_OBJECT_AFFILIATION_MASK) == COMBATLOG_OBJECT_AFFILIATION_PARTY
    @staticmethod
    def isMine(flag):
        return (flag & COMBATLOG_OBJECT_AFFILIATION_MASK) == COMBATLOG_OBJECT_AFFILIATION_MINE
    @staticmethod
    def setOutsider(flag):
        return (flag & ~COMBATLOG_OBJECT_AFFILIATION_MASK) | COMBATLOG_OBJECT_AFFILIATION_OUTSIDER
    @staticmethod
    def setRaid(flag):
        return (flag & ~COMBATLOG_OBJECT_AFFILIATION_MASK) | COMBATLOG_OBJECT_AFFILIATION_RAID
    @staticmethod
    def setParty(flag):
        return (flag & ~COMBATLOG_OBJECT_AFFILIATION_MASK) | COMBATLOG_OBJECT_AFFILIATION_PARTY
    @staticmethod
    def setMine(flag):
        return (flag & ~COMBATLOG_OBJECT_AFFILIATION_MASK) | COMBATLOG_OBJECT_AFFILIATION_MINE
