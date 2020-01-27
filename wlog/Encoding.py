
from enum import Enum

from .Event import Event
from .Encounter import Encounter
from .WLogFile import WLogFile

from .SpellFailed import parseSpellFailed

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
    COMBAT_LOG_VERSION      = 44
    ENCOUNTER_START         = 45
    ENCOUNTER_END           = 46
    COMBATANT_INFO          = 47
    UNIT_DESTROYED          = 48
    UNIT_DISSIPATES         = 49

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
    'UNIT_LOYALTY'           , # 43
    'COMBAT_LOG_VERSION'     , # 44
    'ENCOUNTER_START'        , # 45
    'ENCOUNTER_END'          , # 46
    'COMBATANT_INFO'         , # 47
    'UNIT_DESTROYED'         , # 48
    'UNIT_DISSIPATES'          # 49
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
    def __init__(self, fname):
        self.fname = fname
        self.file = None
        self.nextItemIndex = 1
        self.nextSpellIndex = 1
        self.nextEntityIndex = 1
        self.items = dict()
        self.spells = dict()
        self.entities = dict()
        self.unitFlags = FlagMap()
        self.raidFlags = FlagMap()

    def open(self):
        self.file = open(self.fname, 'wb')

    def close(self):
        self.__writeDictionaries()
        self.file.close()

    def __writeDictionaries(self):
        pass

    def write(self, value):
        if isinstance(value, Event):
            pass
        elif isinstance(value, Encounter):
            pass
        elif isinstance(value, WLogFile):
            pass
        else:
            assert(False)

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

    def miss(self, params) -> bytes:
        assert(len(params) >= 2)
        assert(isinstance(params[0], str))
        assert(isinstance(params[1], str) and (params[1] == 'nil' or params[1] == '1'))

        index = MISS_TYPE.index(params[0])
        assert(index != -1)
        eMissType = MissType(index)

        missType = index.to_bytes(1, byteorder='little')
        isOffHand = 1 if params[1] == '1' else 0
        code = (missType << 1) | isOffHand

        if eMissType == MissType.ABSORB:
            assert(len(params) == 4)
            assert(isinstance(params[2], str))
            assert(isinstance(params[3], str))
            absorbed = encodeDynamic(int(params[2]), size=2)
            critical = encodeDynamic(int(params[3]), size=2)
            return code + absorbed + critical

        elif eMissType == MissType.RESIST or \
             eMissType == MissType.BLOCK:
            assert(len(params) == 3)
            assert(isinstance(params[3], str))
            absorbed = encodeDynamic(int(params[2]), size=2)
            return code + absorbed

        assert(len(params) == 2)
        return code

    def floating(self, value, digits, size, signed=False, dynamic=False) -> bytes:
        if isinstance(value, str):
            value = float(value)
        assert(isinstance(value, float))
        assert(digits is None or isinstance(digits, int))

        if digits is None:
            while int(value) != value:
                value *= 10
            value = int(value)
        else:
            value = int(value * (10 ** digits))
        
        return self.integer(value=value, size=size, signed=signed, dynamic=dynamic)

    def integer(self, value, size, signed=False, dynamic=False) -> bytes:
        if isinstance(value, str):
            if len(value) > 2 and value[:2] == '0x':
                value = int(value, base=16)
            else:
                value = int(value, base=10)
        assert(isinstance(value, int))
        assert(isinstance(size, int))
        assert(size >= 1 and size <= 8)
        assert(isinstance(dynamic, bool))
        assert(value > 0 or signed)

        if signed:
            if value < 0:
                value = ((-value) << 1) | 1
            else:
                value = value << 1

        if dynamic:
            return encodeDynamic(value, size=size)
        return value.to_bytes(length=size, byteorder='little')

    def string(self, value) -> bytes:
        assert(isinstance(value, str))
        return value.encode(encoding='utf-8') + bytes(1)

    def event(self, event) -> bytes:
        eventType = getEventType(event.event)

        src = self.entity(event.srcGUID, event.srcName, event.srcFlags, event.srcRaidFlags)
        dest = self.entity(event.destGUID, event.destName, event.destFlags, event.destRaidFlags)
        code = event.time.encode() + self.integer(int(eventType), size=1) + src + dest

        if eventType == EventType.DAMAGE_SHIELD or \
           eventType == EventType.DAMAGE_SHIELD_MISSED or \
           eventType == EventType.DAMAGE_SPLIT or \
           eventType == EventType.ENCHANT_APPLIED or \
           eventType == EventType.ENCHANT_REMOVED or \
           eventType == EventType.RANGE or \
           eventType == EventType.SPELL:
            code += self.spell(event.prefix_params[0], event.prefix_params[1], event.prefix_params[2])

        elif eventType == EventType.UNIT_DIED or \
             eventType == EventType.UNIT_DESTROYED or \
             eventType == EventType.UNIT_DISSIPATES:
            # recapID, unconsciousOnDeath
            # recapID: The specific death to view, from 1 to the most recent death.
            assert(False) # TODO

        if event.has_advanced_params:
            unit = self.guid(event.unitGUID)
            owner = self.guid(event.ownerGUID)
            currHp = self.integer(event.currHp, size=1)
            assert(event.maxHp == '100')
            assert(event.attackPower == '0')
            assert(event.spellPower == '0')
            assert(event.armor == '0')
            assert(event.resourceType == '-1')
            assert(event.currResource == '0')
            assert(event.maxResource == '0')
            assert(event.resourceCost == '0')
            coord1 = self.floating(event.coord_1, digits=2, size=2)
            coord2 = self.floating(event.coord_2, digits=2, size=2)
            assert(event.UiMapID == '0')
            facing = self.floating(event.facing, digits=4, size=2)
            level = self.integer(event.level, size=1)
            code += unit + owner + currHp + coord1 + coord2 + facing + level

        if eventType == EventType.SPELL_DURABILITY_DAMAGE:
            code += self.item(params[0], params[1])

        elif endsWith(event.event, '_DAMAGE'):
            i = 0
            if eventType == EventType.ENVIRONMENTAL_DAMAGE:
                # environmentalType
                code += self.environmentalType(params[0])
                i = 1
            # 0 amount:
            # 1 ?: 0 - 5000
            # 2 ?: -1 - 2579
            # 3 school: 0 - 127
            # 4 resisted:
            # 5 blocked:
            # 6 absorbed:
            # 7 critical: nil / 1
            # 8 glancing: nil / 1
            # 9 crushing: nil / 1
            amount    = self.integer(event.params[i + 0], size=2, dynamic=True)
            val1      = self.integer(event.params[i + 1], size=2, dynamic=True)
            val2      = self.integer(event.params[i + 2], size=2, dynamic=True)
            school    = self.integer(event.params[i + 3], size=1, dynamic=True)
            resisted  = self.integer(event.params[i + 4], size=2, dynamic=True)
            blocked   = self.integer(event.params[i + 5], size=2, dynamic=True)
            absorbed  = self.integer(event.params[i + 6], size=2, dynamic=True)
            flags     = encodeFlags(event.params[i + 7:])
            code += amount + val1 + val2 + school + resisted + blocked + absorbed + flags

        elif endsWith(event.event, '_MISSED'):
            # missType, isOffHand, amountMissed, critical
            code += self.miss(e.params)

        elif endsWith(event.event, '_HEAL'):
            # amount, overhealing, absorbed, critical
            assert(event.param[0] == event.param[1])
            amount      = self.integer(event.params[1], size=2, dynamic=True)
            overhealing = self.integer(event.params[2], size=2, dynamic=True)
            absorbed    = self.integer(event.params[3], size=2, dynamic=True)
            critical    = encodeFlags(list(event.params[4]))
            code += amount + overhealing + absorbed + critical
        
        elif endsWith(event.event, '_ENERGIZE'):
            # amount, overEnergize, powerType, alternatePowerType
            amount = self.floating(event.params[0], digits=None, size=2, dynamic=True)
            overEnergize = self.floating(event.params[1], digits=None, size=2, dynamic=True)
            powerType = self.integer(event.params[2], size=1)
            powerType = self.integer(event.params[3], size=2, dynamic=True) # dynamic to be safe
        
        elif endsWith(event.event, '_DRAIN') or \
             endsWith(event.event, '_LEECH'):
            # amount, powerType, extraAmount
            assert(len(event.params) == 4)
            assert(int(params[0]) == 50)
            assert(int(params[0]) == 4)
            assert(int(params[0]) == 0)
            assert(int(params[0]) == 1000000)
        
        elif endsWith(event.event, '_INTERRUPT'):
            # extraSpellId, extraSpellName, extraSchool
            code += self.spell(event.params[0], event.params[1], event.params[2])

        elif endsWith(event.event, '_DISPEL'):
            # extraSpellId, extraSpellName, extraSchool, auraType
            code += self.spell(event.params[0], event.params[1], event.params[2])
            code += self.auraType(event.params[3])

        elif endsWith(event.event, '_DISPEL_FAILED'): # TODO >
            # extraSpellId, extraSpellName, extraSchool
            code += self.spell(event.params[0], event.params[1], event.params[2])

        elif endsWith(event.event, '_STOLEN'): # TODO >
            # extraSpellId, extraSpellName, extraSchool, auraType
            code += self.spell(event.params[0], event.params[1], event.params[2])
            code += self.auraType(event.params[3])

        elif endsWith(event.event, '_EXTRA_ATTACKS'):
            # amount
            code += self.integer(event.params[0], size=2, dynamic=True)

        elif endsWith(event.event, '_AURA_APPLIED')      or \
             endsWith(event.event, '_AURA_REMOVED')      or \
             endsWith(event.event, '_AURA_APPLIED_DOSE') or \
             endsWith(event.event, '_AURA_REMOVED_DOSE') or \
             endsWith(event.event, '_AURA_REFRESH'):
            # auraType, amount
            code += self.auraType(event.params[0])
            code += self.integer(event.params[1], size=2, dynamic=True)

        elif endsWith(event.event, '_AURA_BROKEN'):
            # auraType
            code += self.auraType(event.params[0])

        elif endsWith(event.event, '_AURA_BROKEN_SPELL'):
            # extraSpellId, extraSpellName, extraSchool, auraType
            code += self.spell(event.params[0], event.params[1], event.params[2])
            code += self.auraType(event.params[3])

        elif endsWith(event.event, '_CAST_FAILED'):
            # failedType
            index, values = parseSpellFailed(params[0])
            code += self.integer(index, size=2)
            for v in values:
                if isinstance(v, str):
                    code += self.string(v)
                elif isinstance(v, int):
                    code += self.integer(v, size=2, signed=True, dynamic=True)
                else:
                    assert(False)

        elif endsWith(event.event, '_ABSORBED '):
            # amount
            code += self.integer(event.params[1], size=2, dynamic=True)

        else:
            assert(len(event.params) == 0 and 'Parameters were not handled')

        return code

    def __enter__(self):
        self.open()

    def __exit__(self, ex_type, ex_value, ex_traceback):
        if ex_type is not None:
            raise
        self.close()

