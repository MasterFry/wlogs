from .Event import Event
from .EventBase import EventBase
from .EventType import EventType
from .EventParser import EventParser

# 1 :  unitGUID
#       Creature-0-4469-409-26884-11671-0004A8A101
# 2 :  ownerGUID
#       0000000000000000
# 3 :  currHp
#       0
# 4 :  maxHp
#       100 ==> static
# 5 :  attackPower
#       0 ==> static
# 6 :  spellPower
#       0 ==> static
# 7 :  armor
#       0 ==> static
# 8 :  resourceType
#         Enum. PowerType. If there are multiple resource types they are 
#         delimited with a pipe char, e.g. "3|4" for Rogue Energy and ComboPoints.
#       -1 ==> static
# 9 : currResource
#       0 ==> static
# 10: maxResource
#       0 ==> static
# 11: resourceCost
#       0 ==> static
# 12: coord
#       972.03
# 13: coord
#       -948.12
# 14: UiMapID
#       0 ==> static
# 15: facing
#       0.1401
# 16: itemLevel/level
#       61

class EventAdvanced(EventBase):
    def __init__(self, parser: EventParser):
        self.unitGUID = parser.getGUID()    # 1
        self.ownerGUID = parser.getGUID()   # 2
        self.currHP = parser.getInt()       # 3
        assert(parser.getInt() == 100)      # 4
        assert(parser.getInt() == 0)        # 5
        assert(parser.getInt() == 0)        # 6
        assert(parser.getInt() == 0)        # 7
        assert(parser.getInt() == -1)       # 8
        assert(parser.getInt() == 0)        # 9
        assert(parser.getInt() == 0)        # 10
        assert(parser.getInt() == 0)        # 11
        self.coord1 = parser.getFloat()     # 12
        self.coord2 = parser.getFloat()     # 13
        assert(parser.getInt() == 0)        # 14
        self.facing = parser.getFloat()     # 15
        self.level = parser.getInt()        # 16

    def __str__(self):
        return ',{0:s},{1:s},{2:d},100,0,0,0,-1,0,0,0,{3:06.02f},{4:06.02f},0,{5:06.04f},{6:d}'.format(
            str(self.unitGUID),
            str(self.ownerGUID),
            self.currHP,
            self.coord1,
            self.coord2,
            self.facing,
            self.level
        )

    def __eq__(self, other):
        return EventBase.__eq__(other) and \
               self.unitGUID == other.unitGUID and \
               self.ownerGUID == other.ownerGUID

    def __ne__(self, other):
        return not self.__eq__(other)