
from enum import Enum


class EnvironmentalType(Enum):
    DROWNING = 0
    FALLING = 1
    FATIGUE = 2
    FIRE = 3
    LAVA = 4
    SLIM = 5


ENVIRONMENTAIL_TYPE = [
    "Drowning",
    "Falling",
    "Fatigue",
    "Fire",
    "Lava",
    "Slime"
]


class MissType(Enum):
    ABSORB = 0
    BLOCK = 1
    DEFLECT = 2
    DODGE = 3
    EVADE = 4
    IMMUNE = 5
    MISS = 6
    PARRY = 7
    REFLECT = 8
    RESIST = 9


MISS_TYPE = [
    "ABSORB",
    "BLOCK",
    "DEFLECT",
    "DODGE",
    "EVADE",
    "IMMUNE",
    "MISS",
    "PARRY",
    "REFLECT",
    "RESIST"
]


class AuraType(Enum):
    BUFF = 0
    DEBUFF = 1


class EventType(Enum):
    DAMAGE_SHIELD           = 0
    DAMAGE_SHIELD_MISSED    = 1
    DAMAGE_SPLIT            = 2
    ENCHANT_APPLIED         = 3
    ENCHANT_REMOVED         = 4
    ENVIRONMENTAL_DAMAGE    = 5
    PARTY_KILL              = 6
    RANGE_DAMAGE            = 7
    RANGE_MISSED            = 8
    SPELL_ABSORBED          = 9
    SPELL_AURA_APPLIED      = 10
    SPELL_AURA_APPLIED_DOSE = 11
    SPELL_AURA_BROKEN       = 12
    SPELL_AURA_BROKEN_SPELL = 13
    SPELL_AURA_REFRESH      = 14
    SPELL_AURA_REMOVED      = 15
    SPELL_AURA_REMOVED_DOSE = 16
    SPELL_CAST_FAILED       = 17
    SPELL_CAST_START        = 18
    SPELL_CAST_SUCCESS      = 19
    SPELL_CREATE            = 20
    SPELL_DAMAGE            = 21
    SPELL_DURABILITY_DAMAGE = 22
    SPELL_DISPEL            = 23
    SPELL_DRAIN             = 24
    SPELL_ENERGIZE          = 25
    SPELL_EXTRA_ATTACKS     = 26
    SPELL_HEAL              = 27
    SPELL_INSTAKILL         = 28
    SPELL_INTERRUPT         = 29
    SPELL_MISSED            = 30
    SPELL_PERIODIC_DAMAGE   = 31
    SPELL_PERIODIC_DRAIN    = 32
    SPELL_PERIODIC_ENERGIZE = 33
    SPELL_PERIODIC_HEAL     = 34
    SPELL_PERIODIC_LEECH    = 35
    SPELL_PERIODIC_MISSED   = 36
    SPELL_RESURRECT         = 37
    SPELL_SUMMON            = 38
    SWING_DAMAGE            = 39
    SWING_DAMAGE_LANDED     = 40
    SWING_MISSED            = 41
    UNIT_DIED               = 42
    UNIT_LOYALTY            = 43

EVENT_NAMES = [
    'DAMAGE_SHIELD'          , # 0
    'DAMAGE_SHIELD_MISSED'   , # 1
    'DAMAGE_SPLIT'           , # 2
    'ENCHANT_APPLIED'        , # 3
    'ENCHANT_REMOVED'        , # 4
    'ENVIRONMENTAL_DAMAGE'   , # 5
    'PARTY_KILL'             , # 6
    'RANGE_DAMAGE'           , # 7
    'RANGE_MISSED'           , # 8
    'SPELL_ABSORBED'         , # 9
    'SPELL_AURA_APPLIED'     , # 10
    'SPELL_AURA_APPLIED_DOSE', # 11
    'SPELL_AURA_BROKEN'      , # 12
    'SPELL_AURA_BROKEN_SPELL', # 13
    'SPELL_AURA_REFRESH'     , # 14
    'SPELL_AURA_REMOVED'     , # 15
    'SPELL_AURA_REMOVED_DOSE', # 16
    'SPELL_CAST_FAILED'      , # 17
    'SPELL_CAST_START'       , # 18
    'SPELL_CAST_SUCCESS'     , # 19
    'SPELL_CREATE'           , # 20
    'SPELL_DAMAGE'           , # 21
    'SPELL_DURABILITY_DAMAGE', # 22
    'SPELL_DISPEL'           , # 23
    'SPELL_DRAIN'            , # 24
    'SPELL_ENERGIZE'         , # 25
    'SPELL_EXTRA_ATTACKS'    , # 26
    'SPELL_HEAL'             , # 27
    'SPELL_INSTAKILL'        , # 28
    'SPELL_INTERRUPT'        , # 29
    'SPELL_MISSED'           , # 30
    'SPELL_PERIODIC_DAMAGE'  , # 31
    'SPELL_PERIODIC_DRAIN'   , # 32
    'SPELL_PERIODIC_ENERGIZE', # 33
    'SPELL_PERIODIC_HEAL'    , # 34
    'SPELL_PERIODIC_LEECH'   , # 35
    'SPELL_PERIODIC_MISSED'  , # 36
    'SPELL_RESURRECT'        , # 37
    'SPELL_SUMMON'           , # 38
    'SWING_DAMAGE'           , # 39
    'SWING_DAMAGE_LANDED'    , # 40
    'SWING_MISSED'           , # 41
    'UNIT_DIED'              , # 42
    'UNIT_LOYALTY'             # 43
]


def getEventType(name: str) -> EventType:
    assert(name in EVENT_NAMES)
    return EventType(EVENT_NAMES.index(name))


def getEventName(eventType: EventType) -> str:
    return EVENT_NAMES[int(eventType)]


def encodeDynamic(value: int, size: int = 1) -> bytes:
        assert(size > 1 and size <= 16)
        if value == 0:
            return bytes(1)
        
        shift = 7 + ((size - 1) << 3)
        flag = 1 << shift
        mask = ~flag

        code = b''
        while value > 0:
            v = value & mask
            value = value >> shift
            if value > 0:
                v |= flag
            code += (value & mask).to_bytes(length=1, byteorder='little')
        
        return code


def encodeFlags(args: list):
    for i in range(len(args)):
        if args[i] == 'nil':
            args[i] = 0
        elif args[i] == '1':
            args[i] = 1
        else:
            assert(False)
    
    index = 0
    code = b''
    while index < len(args):
        c = 0
        i = 0
        while i < 8 and index < len(args):
            c = (c << 1) | args[index]
            index += 1
            i += 1
        code += c.to_bytes(1, byteorder='little')
    
    return code


class FlagMap:
    def __init__(self):
        self.map = list()
        
    def encode(self, flag) -> bytes:
        if flag not in self.map:
            self.map.append(flag)
        return self.map.index(flag).to_bytes(1, byteorder='little')


class EncodingEntity:
    def __init__(self, index, name):
        self.index = index
        self.name = name


class EncodingItem:
    def __init__(self, index, name):
        self.index = index
        self.name = name


class EncodingSpell:
    def __init__(self, index, name, school):
        self.index = index
        self.name = name
        self.school = school


class Encoder:
    def __init__(self):
        self.nextItemIndex = 1
        self.nextSpellIndex = 1
        self.nextEntityIndex = 1
        self.items = dict()
        self.spells = dict()
        self.entities = dict()
        self.unitFlags = FlagMap()
        self.raidFlags = FlagMap()

    def guid(self, guid) -> bytes:
        assert(isinstance(guid, str))
        if guid == '0000000000000000':
            return bytes(1)
        if guid not in self.entities:
            self.entities[guid] = EncodingEntity(self.nextEntityIndex, None)
            self.nextEntityIndex += 1
        return Encoder.encodeDynamic(self.entities[guid].index, size=1)

    def item(self, itemId, name) -> bytes:
        assert(isinstance(itemId, str))
        assert(isinstance(name, str))

        if itemId not in self.items:
            self.items[itemId] = EncodingItem(self.nextItemIndex, name.strip(""))
            self.nextItemIndex += 1
        return Encoder.encodeDynamic(self.items[itemId].index, size=1)
    
    def spell(self, spellId, name, spellSchool) -> bytes:
        assert(isinstance(spellId, str))
        if isinstance(spellSchool, str):
            spellSchool = int(spellSchool)
        assert(isinstance(spellSchool, int))
        assert(isinstance(name, str))

        if spellId not in self.spells:
            self.spells[spellId] = EncodingSpell(self.nextSpellIndex, name.strip(""), spellSchool)
            self.nextSpellIndex += 1
        return Encoder.encodeDynamic(self.spells[spellId].index, size=1)

    def entity(self, guid, name, unitFlags, raidFlags) -> bytes:
        assert(isinstance(guid, str))
        if guid == '0000000000000000':
            return bytes(1)

        if isinstance(unitFlags, str):
            unitFlags = int(unitFlags, 16)
        if isinstance(raidFlags, str):
            raidFlags = int(raidFlags, 16)
        assert(isinstance(unitFlags, int))
        assert(isinstance(raidFlags, int))
        flags = self.unitFlags.encode(unitFlags) + self.raidFlags.encode(raidFlags)

        assert(isinstance(name, str))
        if guid not in self.entities:
            self.entities[guid] = EncodingEntity(self.nextEntityIndex, name.strip('"'))
            self.nextEntityIndex += 1
        elif self.entities[guid].name is None:
            self.entities[guid].name = name
        return Encoder.encodeDynamic(self.entities[guid].index, size=1) + flags

    def auraType(self, auraType) -> bytes:
        assert(isinstance(auraType, str))
        if auraType == 'BUFF':
            return AuraType.BUFF.to_bytes(1, byteorder='little')
        if auraType == 'DEBUFF':
            return AuraType.DEBUFF.to_bytes(1, byteorder='little')
        assert(False and 'Invalid aura type: %s' % auraType)

    def environmentalType(self, environmentalType) -> bytes:
        assert(isinstance(environmentalType, str))
        index = ENVIRONMENTAIL_TYPE.index(environmentalType)
        assert(index != -1)
        return index.to_bytes(1, byteorder='little')
