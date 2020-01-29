from .EventDamageShield import EventDamageShield
from .EventDamageShieldMissed import EventDamageShieldMissed
from .EventDamageSplit import EventDamageSplit
from .EventEnchantApplied import EventEnchantApplied
from .EventEnchantRemoved import EventEnchantRemoved
from .EventEnvironmentalDamage import EventEnvironmentalDamage
from .EventPartyKill import EventPartyKill
from .EventRangeDamage import EventRangeDamage
from .EventRangeMissed import EventRangeMissed
from .EventSpellAbsorbed import EventSpellAbsorbed
from .EventSpellAuraApplied import EventSpellAuraApplied
from .EventSpellAuraAppliedDose import EventSpellAuraAppliedDose
from .EventSpellAuraBroken import EventSpellAuraBroken
from .EventSpellAuraBrokenSpell import EventSpellAuraBrokenSpell
from .EventSpellAuraRefresh import EventSpellAuraRefresh
from .EventSpellAuraRemoved import EventSpellAuraRemoved
from .EventSpellAuraRemovedDose import EventSpellAuraRemovedDose
from .EventSpellCastFailed import EventSpellCastFailed
from .EventSpellCastStart import EventSpellCastStart
from .EventSpellCastSuccess import EventSpellCastSuccess
from .EventSpellCreate import EventSpellCreate
from .EventSpellDamage import EventSpellDamage
from .EventSpellDurabilityDamage import EventSpellDurabilityDamage
from .EventSpellDispel import EventSpellDispel
from .EventSpellDrain import EventSpellDrain
from .EventSpellEnergize import EventSpellEnergize
from .EventSpellExtraAttacks import EventSpellExtraAttacks
from .EventSpellHeal import EventSpellHeal
from .EventSpellInstakill import EventSpellInstakill
from .EventSpellInterrupt import EventSpellInterrupt
from .EventSpellMissed import EventSpellMissed
from .EventSpellPeriodicDamage import EventSpellPeriodicDamage
from .EventSpellPeriodicDrain import EventSpellPeriodicDrain
from .EventSpellPeriodicEnergize import EventSpellPeriodicEnergize
from .EventSpellPeriodicHeal import EventSpellPeriodicHeal
from .EventSpellPeriodicLeech import EventSpellPeriodicLeech
from .EventSpellPeriodicMissed import EventSpellPeriodicMissed
from .EventSpellResurrect import EventSpellResurrect
from .EventSpellSummon import EventSpellSummon
from .EventSwingDamage import EventSwingDamage
from .EventSwingDamageLanded import EventSwingDamageLanded
from .EventSwingMissed import EventSwingMissed
from .EventUnitDied import EventUnitDied
from .EventUnitLoyalty import EventUnitLoyalty
from .EventCombatLogVersion import EventCombatLogVersion
from .EventEncounterStart import EventEncounterStart
from .EventEncounterEnd import EventEncounterEnd
from .EventCombatantInfo import EventCombatantInfo
# from .EventUnitDestroyed import EventUnitDestroyed
# from .EventUnitDissipates import EventUnitDissipates

EVENT_TABLE = { 
    'DAMAGE_SHIELD'          : EventDamageShield,
    'DAMAGE_SHIELD_MISSED'   : EventDamageShieldMissed,
    'DAMAGE_SPLIT'           : EventDamageSplit,
    'ENCHANT_APPLIED'        : EventEnchantApplied,
    'ENCHANT_REMOVED'        : EventEnchantRemoved,
    'ENVIRONMENTAL_DAMAGE'   : EventEnvironmentalDamage,
    'PARTY_KILL'             : EventPartyKill,
    'RANGE_DAMAGE'           : EventRangeDamage,
    'RANGE_MISSED'           : EventRangeMissed,
    'SPELL_ABSORBED'         : EventSpellAbsorbed,
    'SPELL_AURA_APPLIED'     : EventSpellAuraApplied,
    'SPELL_AURA_APPLIED_DOSE': EventSpellAuraAppliedDose,
    'SPELL_AURA_BROKEN'      : EventSpellAuraBroken,
    'SPELL_AURA_BROKEN_SPELL': EventSpellAuraBrokenSpell,
    'SPELL_AURA_REFRESH'     : EventSpellAuraRefresh,
    'SPELL_AURA_REMOVED'     : EventSpellAuraRemoved,
    'SPELL_AURA_REMOVED_DOSE': EventSpellAuraRemovedDose,
    'SPELL_CAST_FAILED'      : EventSpellCastFailed,
    'SPELL_CAST_START'       : EventSpellCastStart,
    'SPELL_CAST_SUCCESS'     : EventSpellCastSuccess,
    'SPELL_CREATE'           : EventSpellCreate,
    'SPELL_DAMAGE'           : EventSpellDamage,
    'SPELL_DURABILITY_DAMAGE': EventSpellDurabilityDamage,
    'SPELL_DISPEL'           : EventSpellDispel,
    'SPELL_DRAIN'            : EventSpellDrain,
    'SPELL_ENERGIZE'         : EventSpellEnergize,
    'SPELL_EXTRA_ATTACKS'    : EventSpellExtraAttacks,
    'SPELL_HEAL'             : EventSpellHeal,
    'SPELL_INSTAKILL'        : EventSpellInstakill,
    'SPELL_INTERRUPT'        : EventSpellInterrupt,
    'SPELL_MISSED'           : EventSpellMissed,
    'SPELL_PERIODIC_DAMAGE'  : EventSpellPeriodicDamage,
    'SPELL_PERIODIC_DRAIN'   : EventSpellPeriodicDrain,
    'SPELL_PERIODIC_ENERGIZE': EventSpellPeriodicEnergize,
    'SPELL_PERIODIC_HEAL'    : EventSpellPeriodicHeal,
    'SPELL_PERIODIC_LEECH'   : EventSpellPeriodicLeech,
    'SPELL_PERIODIC_MISSED'  : EventSpellPeriodicMissed,
    'SPELL_RESURRECT'        : EventSpellResurrect,
    'SPELL_SUMMON'           : EventSpellSummon,
    'SWING_DAMAGE'           : EventSwingDamage,
    'SWING_DAMAGE_LANDED'    : EventSwingDamageLanded,
    'SWING_MISSED'           : EventSwingMissed,
    'UNIT_DIED'              : EventUnitDied,
    'UNIT_LOYALTY'           : EventUnitLoyalty,
    'COMBAT_LOG_VERSION'     : EventCombatLogVersion,
    'ENCOUNTER_START'        : EventEncounterStart,
    'ENCOUNTER_END'          : EventEncounterEnd,
    'COMBATANT_INFO'         : EventCombatantInfo,
    'UNIT_DESTROYED'         : None,
    'UNIT_DISSIPATES'        : None
}