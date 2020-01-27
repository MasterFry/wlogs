from enum import IntEnum

from .Encode import encodeInt

class AuraType(IntEnum):
    BUFF   = 0
    DEBUFF = 1


AURA_TYPE_NAMES = [
    'BUFF'  ,   # 0
    'DEBUFF'    # 1
]


def getAuraTypeName(index) -> str:
    return AURA_TYPE_NAMES[int(index)]


def encodeAuraType(auraType: AuraType) -> bytes:
    return encodeInt(int(auraType), size=1)
