from enum import IntEnum

class AuraType(IntEnum):
    BUFF   = 0
    DEBUFF = 1


AURA_TYPE_NAMES = [
    'BUFF'  ,   # 0
    'DEBUFF'    # 1
]


def getAuraTypeName(index) -> str:
    return AURA_TYPE_NAMES[int(index)]
