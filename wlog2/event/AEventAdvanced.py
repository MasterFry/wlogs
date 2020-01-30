
from ..types import EventType
from ..types import GUIDType
from ..encode.AEncoder import AEncoder
from ..encode.ADecoder import ADecoder
from ..encode.SizeType import SizeType

from ..EventParser import EventParser

from .AEventBase import AEventBase

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

class AEventAdvanced(AEventBase):
    def __init__(self, parser):
        if isinstance(parser, EventParser):
            self.unitGUID = parser.getGUID()  # 1
            self.ownerGUID = parser.getGUID() # 2
            self.currHP = parser.getInt()     # 3
            maxHP = parser.getInt()           # 4
            assert(maxHP == 100 or (maxHP == 0 and self.unitGUID.guidType == GUIDType.NULL))
            assert(parser.getInt() == 0)      # 5
            assert(parser.getInt() == 0)      # 6
            assert(parser.getInt() == 0)      # 7
            assert(parser.getInt() == -1)     # 8
            assert(parser.getInt() == 0)      # 9
            assert(parser.getInt() == 0)      # 10
            assert(parser.getInt() == 0)      # 11
            self.coord1 = parser.getFloat()   # 12
            self.coord2 = parser.getFloat()   # 13
            self.mapId = parser.getInt()      # 14
            self.facing = parser.getFloat()   # 15
            self.level = parser.getInt()      # 16
            
        elif isinstance(parser, ADecoder):
            self.decode(decode)
        else:
            ValueError('Parser not supported: ' + type(parser))

    def decode(self, decoder: ADecoder):
        self.unitGUID = decoder.guid()
        self.ownerGUID = decoder.guid()
        self.currHP = decoder.integer(size=SizeType.HP)
        self.coord1 = decoder.floating(size=SizeType.COORDINATE, digits=2, signed=True)
        self.coord2 = decoder.floating(size=SizeType.COORDINATE, digits=2, signed=True)
        self.mapId = decoder.integer(size=SizeType.MAP_ID)
        self.facing = decoder.floating(size=SizeType.FACING, digits=4)
        self.level = decoder.integer(size=SizeType.LEVEL)

    def encode(self, encoder: AEncoder) -> bytes:
        return encoder.guid(self.unitGUID) + \
               encoder.guid(self.ownerGUID) + \
               encoder.integer(self.currHP, size=SizeType.HP) + \
               encoder.floating(self.coord1, size=SizeType.COORDINATE, digits=2, signed=True) + \
               encoder.floating(self.coord2, size=SizeType.COORDINATE, digits=2, signed=True) + \
               encoder.integer(self.mapId, size=SizeType.MAP_ID) + \
               encoder.floating(self.facing, size=SizeType.FACING, digits=4) + \
               encoder.integer(self.level, size=SizeType.LEVEL)

    def __str__(self):
        return ',{0:s},{1:s},{2:d},{3:s},0,0,0,-1,0,0,0,{4:.02f},{5:.02f},{6:d},{7:.04f},{8:d}'.format(
            str(self.unitGUID),
            str(self.ownerGUID),
            self.currHP,
            '0' if self.unitGUID.guidType == GUIDType.NULL else '100', # maxHP
            self.coord1,
            self.coord2,
            self.mapId,
            self.facing,
            self.level
        )

    def __eq__(self, other):
        return AEventBase.__eq__(self, other) and \
               self.unitGUID == other.unitGUID and \
               self.ownerGUID == other.ownerGUID and \
               self.mapId == other.mapId

    def __ne__(self, other):
        return not self.__eq__(other)