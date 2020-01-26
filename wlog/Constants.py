# Information from:
# https://wow.gamepedia.com/COMBAT_LOG_EVENT

# Parameter count for different events
PARAM_COUNT = {
    'DAMAGE_SHIELD'           : 43 ,
    'DAMAGE_SHIELD_MISSED'    : 20 ,
    'DAMAGE_SPLIT'            : 43 ,
    'ENCHANT_APPLIED'         : 17 ,
    'ENCHANT_REMOVED'         : 17 ,
    'ENVIRONMENTAL_DAMAGE'    : 41 ,
    'PARTY_KILL'              : 14 ,
    'RANGE_DAMAGE'            : 43 ,
    'RANGE_MISSED'            : 20 ,
    'SPELL_ABSORBED'          : 26 ,
    'SPELL_AURA_APPLIED'      : 18 ,
    'SPELL_AURA_APPLIED_DOSE' : 19 ,
    'SPELL_AURA_BROKEN'       : 18 ,
    'SPELL_AURA_BROKEN_SPELL' : 21 ,
    'SPELL_AURA_REFRESH'      : 18 ,
    'SPELL_AURA_REMOVED'      : 18 ,
    'SPELL_AURA_REMOVED_DOSE' : 19 ,
    'SPELL_CAST_FAILED'       : 18 ,
    'SPELL_CAST_START'        : 17 ,
    'SPELL_CAST_SUCCESS'      : 33 ,
    'SPELL_CREATE'            : 17 ,
    'SPELL_DAMAGE'            : 43 ,
    'SPELL_DURABILITY_DAMAGE' : 19 ,
    'SPELL_DISPEL'            : 21 ,
    'SPELL_DRAIN'             : 37 ,
    'SPELL_ENERGIZE'          : 37 ,
    'SPELL_EXTRA_ATTACKS'     : 18 ,
    'SPELL_HEAL'              : 38 ,
    'SPELL_INSTAKILL'         : 17 ,
    'SPELL_INTERRUPT'         : 20 ,
    'SPELL_MISSED'            : 20 ,
    'SPELL_PERIODIC_DAMAGE'   : 43 ,
    'SPELL_PERIODIC_DRAIN'    : 37 ,
    'SPELL_PERIODIC_ENERGIZE' : 37 ,
    'SPELL_PERIODIC_HEAL'     : 38 ,
    'SPELL_PERIODIC_LEECH'    : 37 ,
    'SPELL_PERIODIC_MISSED'   : 19 ,
    'SPELL_RESURRECT'         : 17 ,
    'SPELL_SUMMON'            : 17 ,
    'SWING_DAMAGE'            : 40 ,
    'SWING_DAMAGE_LANDED'     : 40 ,
    'SWING_MISSED'            : 16 ,
    'UNIT_DIED'               : 14 ,
    'UNIT_LOYALTY'            : 15 
}

# Prefix Parameter count for different events
PREFIX_PARAM_COUNT = {
    'DAMAGE_SHIELD'        : 3 ,
    'DAMAGE_SHIELD_MISSED' : 3 ,
    'DAMAGE_SPLIT'         : 3 ,
    'ENCHANT_APPLIED'      : 3 ,
    'ENCHANT_REMOVED'      : 3 ,
    'ENVIRONMENTAL'        : 0 , # Environmental type is after Advanced Parameters
    'PARTY_KILL'           : 0 ,
    'RANGE'                : 3 ,
    'SPELL'                : 3 ,
    'SWING'                : 0 ,
    'UNIT_DESTROYED'       : 2 ,
    'UNIT_DIED'            : 0 ,
    'UNIT_DISSIPATES'      : 2 ,
    'UNIT_LOYALTY'         : 0 
}