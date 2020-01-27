from enum import IntEnum

from .Encode import encodeInt

class EventType(IntEnum):
    COMBATANT_INFO          = 0
    COMBAT_LOG_VERSION      = 1
    DAMAGE_SHIELD           = 2
    DAMAGE_SHIELD_MISSED    = 3
    DAMAGE_SPLIT            = 4
    ENCHANT_APPLIED         = 5
    ENCHANT_REMOVED         = 6
    ENCOUNTER_END           = 7
    ENCOUNTER_START         = 8
    ENVIRONMENTAL_DAMAGE    = 9
    PARTY_KILL              = 10
    RANGE_DAMAGE            = 11
    RANGE_MISSED            = 12
    SPELL_ABSORBED          = 13
    SPELL_AURA_APPLIED      = 14
    SPELL_AURA_APPLIED_DOSE = 15
    SPELL_AURA_BROKEN       = 16
    SPELL_AURA_BROKEN_SPELL = 17
    SPELL_AURA_REFRESH      = 18
    SPELL_AURA_REMOVED      = 19
    SPELL_AURA_REMOVED_DOSE = 20
    SPELL_CAST_FAILED       = 21
    SPELL_CAST_START        = 22
    SPELL_CAST_SUCCESS      = 23
    SPELL_CREATE            = 24
    SPELL_DAMAGE            = 25
    SPELL_DISPEL            = 26
    SPELL_DRAIN             = 27
    SPELL_DURABILITY_DAMAGE = 28
    SPELL_ENERGIZE          = 29
    SPELL_EXTRA_ATTACKS     = 30
    SPELL_HEAL              = 31
    SPELL_INSTAKILL         = 32
    SPELL_INTERRUPT         = 33
    SPELL_MISSED            = 34
    SPELL_PERIODIC_DAMAGE   = 35
    SPELL_PERIODIC_DRAIN    = 36
    SPELL_PERIODIC_ENERGIZE = 37
    SPELL_PERIODIC_HEAL     = 38
    SPELL_PERIODIC_LEECH    = 39
    SPELL_PERIODIC_MISSED   = 40
    SPELL_RESURRECT         = 41
    SPELL_SUMMON            = 42
    SWING_DAMAGE            = 43
    SWING_DAMAGE_LANDED     = 44
    SWING_MISSED            = 45
    UNIT_DESTROYED          = 46
    UNIT_DIED               = 47
    UNIT_DISSIPATES         = 48
    UNIT_LOYALTY            = 49

EVENT_NAMES = [
    'COMBATANT_INFO'          , # 0
    'COMBAT_LOG_VERSION'      , # 1
    'DAMAGE_SHIELD'           , # 2
    'DAMAGE_SHIELD_MISSED'    , # 3
    'DAMAGE_SPLIT'            , # 4
    'ENCHANT_APPLIED'         , # 5
    'ENCHANT_REMOVED'         , # 6
    'ENCOUNTER_END'           , # 7
    'ENCOUNTER_START'         , # 8
    'ENVIRONMENTAL_DAMAGE'    , # 9
    'PARTY_KILL'              , # 10
    'RANGE_DAMAGE'            , # 11
    'RANGE_MISSED'            , # 12
    'SPELL_ABSORBED'          , # 13
    'SPELL_AURA_APPLIED'      , # 14
    'SPELL_AURA_APPLIED_DOSE' , # 15
    'SPELL_AURA_BROKEN'       , # 16
    'SPELL_AURA_BROKEN_SPELL' , # 17
    'SPELL_AURA_REFRESH'      , # 18
    'SPELL_AURA_REMOVED'      , # 19
    'SPELL_AURA_REMOVED_DOSE' , # 20
    'SPELL_CAST_FAILED'       , # 21
    'SPELL_CAST_START'        , # 22
    'SPELL_CAST_SUCCESS'      , # 23
    'SPELL_CREATE'            , # 24
    'SPELL_DAMAGE'            , # 25
    'SPELL_DISPEL'            , # 26
    'SPELL_DRAIN'             , # 27
    'SPELL_DURABILITY_DAMAGE' , # 28
    'SPELL_ENERGIZE'          , # 29
    'SPELL_EXTRA_ATTACKS'     , # 30
    'SPELL_HEAL'              , # 31
    'SPELL_INSTAKILL'         , # 32
    'SPELL_INTERRUPT'         , # 33
    'SPELL_MISSED'            , # 34
    'SPELL_PERIODIC_DAMAGE'   , # 35
    'SPELL_PERIODIC_DRAIN'    , # 36
    'SPELL_PERIODIC_ENERGIZE' , # 37
    'SPELL_PERIODIC_HEAL'     , # 38
    'SPELL_PERIODIC_LEECH'    , # 39
    'SPELL_PERIODIC_MISSED'   , # 40
    'SPELL_RESURRECT'         , # 41
    'SPELL_SUMMON'            , # 42
    'SWING_DAMAGE'            , # 43
    'SWING_DAMAGE_LANDED'     , # 44
    'SWING_MISSED'            , # 45
    'UNIT_DESTROYED'          , # 46
    'UNIT_DIED'               , # 47
    'UNIT_DISSIPATES'         , # 48
    'UNIT_LOYALTY'              # 49
]


def getEventName(index) -> str:
    return EVENT_NAMES[int(index)]


def encodeEventType(eventType: EventType) -> bytes:
    return encodeInt(int(eventType), size=1)
