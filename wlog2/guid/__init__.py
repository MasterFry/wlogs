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
