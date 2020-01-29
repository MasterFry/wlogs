from .AGUID import AGUID
from .GUIDNull import GUIDNull
from .GUIDPlayer import GUIDPlayer
from .GUIDCreature import GUIDCreature
from .GUIDPet import GUIDPet
from .GUIDGameObject import GUIDGameObject
from .GUIDVehicle import GUIDVehicle
from .GUIDVignette import GUIDVignette
from .GUIDItem import GUIDItem
from .GUIDCorpse import GUIDCorpse

GUID_TABLE = {
    '0000000000000000': GUIDNull,
    'Player'          : GUIDPlayer,
    'Creature'        : GUIDCreature,
    'Pet'             : GUIDPet,
    'GameObject'      : GUIDGameObject,
    'Vehicle'         : GUIDVehicle,
    'Vignette'        : GUIDVignette,
    'Item'            : GUIDItem,
    'Corpse'          : GUIDCorpse
}

from re import compile

REGEX_GUID = compile('(0{16})|(Player-[0-9]+-[0-9A-F]{8})|(Item-[0-9]+-0-[0-9A-F]{16})|((Corpse|Creature|GameObject|Pet|Vehicle|Vignette)-0-[0-9]+-[0-9]+-[0-9]+-[0-9]+-[0-9A-F]{10})')

def isGUID(string) -> bool:
    return REGEX_GUID.match(string) is not None
