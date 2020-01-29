from enum import IntEnum

class GUIDType(IntEnum):
    NULL = 0
    PLAYER = 1
    CREATURE = 2
    PET = 3
    GAME_OBJECT = 4
    VEHICLE = 5
    VIGNETTE = 6
    ITEM = 7
    CORPSE = 8

GUID_TYPE_NAMES = [
    '0000000000000000',
    'Player',
    'Creature',
    'Pet',
    'GameObject',
    'Vehicle',
    'Vignette',
    'Item',
    'Corpse'
]

def getGUIDTypeName(guidType: GUIDType) -> str:
    return GUID_TYPE_NAMES[guidType]