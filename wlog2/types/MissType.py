from enum import IntEnum

class MissType(IntEnum):
    ABSORB  = 0
    BLOCK   = 1
    DEFLECT = 2
    DODGE   = 3
    EVADE   = 4
    IMMUNE  = 5
    MISS    = 6
    PARRY   = 7
    REFLECT = 8
    RESIST  = 9


MISS_TYPE_NAMES = [
    "ABSORB" , # 0
    "BLOCK"  , # 1
    "DEFLECT", # 2
    "DODGE"  , # 3
    "EVADE"  , # 4
    "IMMUNE" , # 5
    "MISS"   , # 6
    "PARRY"  , # 7
    "REFLECT", # 8
    "RESIST"   # 9
]


def getMissTypeName(missType: MissType) -> str:
    return missType.name
