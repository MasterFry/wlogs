from enum import Enum


class AuraType(Enum):
    BUFF = 0
    DEBUFF = 1


AURA_NAMES = [
    'BUFF',     # 0
    'DEBUFF'    # 1
]


def getAuraName(index) -> str:
    return AURA_NAMES[int(index)]
