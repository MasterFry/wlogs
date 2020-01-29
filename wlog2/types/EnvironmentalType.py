from enum import IntEnum

class EnvironmentalType(IntEnum):
    DROWNING = 0
    FALLING = 1
    FATIGUE = 2
    FIRE = 3
    LAVA = 4
    SLIM = 5


ENVIRONMENTAIL_TYPE_NAMES = [
    "Drowning",
    "Falling",
    "Fatigue",
    "Fire",
    "Lava",
    "Slime"
]


def getEnvironmentalTypeName(index) -> str:
    return ENVIRONMENTAIL_TYPE_NAMES[int(index)]
