from .Buffs import PlayerBuffs
from .Encounter import Encounter
from .Event import Event
from .GUID import GUID
from .Time import Time
from .UnitFlag import UnitFlag
from .WLogFile import WLogFile

from .Lua import LuaObjectError
from .Lua import parseLuaObject

from .Utils import CorruptionError
from .Utils import AdvancedLoggingError
from .Utils import wlog_split_line
from .Utils import endsWith

from .Constants import PARAM_COUNT
from .Constants import PREFIX_PARAM_COUNT

from .Merger import Merger


# 1/20 20:34:51.059  
# SWING_DAMAGE,
# Player-4701-008838B8,"Jexx-Mograine",0x40514,0x1,
# Creature-0-4447-249-12442-10184-000025FBAB,"Onyxia",0xa48,0x80,
# Player-4701-008838B8,0000000000000000,
# 95,100,0,0,0,-1,0,0,0,-43.61,-214.18,0,0.1113,66,131,250,-1,1,0,0,0,nil,1,nil

"""
================================== Combat Log Event ==================================
In version 10 there can be up to 38 parameters:
9 base parameters from CLEU (event, source unit and dest unit)
0-3 prefix params from CLEU (spell/environmental events)
16 advanced parameters which require CVar advancedCombatLogging to be enabled for meaningful values.
10 suffix params from CLEU

================================== Base Parameters ==================================
1.  timestamp
2.  event
    (hideCaster) ==> Not used?
3.  sourceGUID
4.  sourceName
5.  sourceFlags
6.  sourceRaidFlags
7.  destGUID
8.  destName
9.  destFlags
10. destRaidFlags

================================== Prefixes ==================================
The Parameters listed with prefixes are numbered in the order they come after the 11 base parameters.
                12                  13                  14
SWING
RANGE           spellId             spellName           spellSchool
SPELL           spellId             spellName           spellSchool
SPELL_PERIODIC  spellId             spellName           spellSchool
SPELL_BUILDING  spellId             spellName           spellSchool
ENVIRONMENTAL   environmentalType

================================== Suffixes ==================================
The Parameters listed with suffixes are numbered in the order they come after the prefix parameters.

Note that params for SWING_DAMAGE start at the 12th parameter; and for ENVIRONMENTAL_DAMAGE at the 13th parameter.
The parameters for critical, glancing, crushing, and isOffHand are true/false flags.

                    15              16              17              18          19          20          21          22          23          24
_DAMAGE             amount          ?               ?               school      ?           ?           ?           critical    glancing    crushing
WRONG:
_DAMAGE             amount          overkill        school          resisted    blocked     absorbed    critical    glancing    crushing    isOffHand
_MISSED             missType        isOffHand       amountMissed    critical
_HEAL               amount          overhealing     absorbed        critical
_ENERGIZE           amount          overEnergize    powerType       alternatePowerType
_DRAIN              amount          powerType       extraAmount
_LEECH              amount          powerType       extraAmount
_INTERRUPT          extraSpellId    extraSpellName  extraSchool
_DISPEL             extraSpellId    extraSpellName  extraSchool     auraType
_DISPEL_FAILED      extraSpellId    extraSpellName  extraSchool
_STOLEN             extraSpellId    extraSpellName  extraSchool     auraType
_EXTRA_ATTACKS      amount
_AURA_APPLIED       auraType        amount
_AURA_REMOVED       auraType        amount
_AURA_APPLIED_DOSE  auraType        amount
_AURA_REMOVED_DOSE  auraType        amount
_AURA_REFRESH       auraType        amount
_AURA_BROKEN        auraType
_AURA_BROKEN_SPELL  extraSpellId    extraSpellName  extraSchool     auraType
_CAST_START
_CAST_SUCCESS
_CAST_FAILED        failedType
_INSTAKILL
_DURABILITY_DAMAGE
_DURABILITY_DAMAGE_ALL
_CREATE
_SUMMON
_RESURRECT
_ABSORBED           amount

================================== Advanced parameters ==================================
1.  unitGUID
2.  ownerGUID
3.  currHp
4.  maxHp
5.  attackPower
6.  spellPower
7.  armor
8.  resourceType
        Enum. PowerType. If there are multiple resource types they are 
        delimited with a pipe char, e.g. "3|4" for Rogue Energy and ComboPoints.
9.  currResource
10. maxResource
11. resourceCost
12. coord
13. coord
14. UiMapID
15. facing
16. itemLevel/level

================================== Special Events ==================================
                     Prefix to use Suffix to use
DAMAGE_SHIELD         SPELL         _DAMAGE
DAMAGE_SPLIT         SPELL         _DAMAGE
DAMAGE_SHIELD_MISSED SPELL         _MISSED

                    12          13                  14
ENCHANT_APPLIED     spellName itemID             itemName
ENCHANT_REMOVED     spellName itemID             itemName
PARTY_KILL
UNIT_DIED         recapID     unconsciousOnDeath
UNIT_DESTROYED     recapID     unconsciousOnDeath
UNIT_DISSIPATES     recapID     unconsciousOnDeath

================================== GUID ==================================
For players: 
    Player-[server ID]-[player UID] 
    (Example: "Player-970-0002FD64")
For creatures, pets, objects, and vehicles: 
    [Unit type]-0-[server ID]-[instance ID]-[zone UID]-[ID]-[spawn UID] 
    (Example: "Creature-0-970-0-11-31146-000136DF91")
Unit Type Names: 
    "Creature", "Pet", "GameObject", "Vehicle", and "Vignette"
For items: 
    Item-[server ID]-0-[spawn UID]
    (Example: "Item-970-0-400000076620BFF4") 
    (Please note that this tells you nothing useful about the item, like the ID)

================================== Unit Flag ==================================
- Type
    COMBATLOG_OBJECT_TYPE_MASK              0x0000FC00
    COMBATLOG_OBJECT_TYPE_OBJECT            0x00004000
    COMBATLOG_OBJECT_TYPE_GUARDIAN          0x00002000
    COMBATLOG_OBJECT_TYPE_PET               0x00001000
    COMBATLOG_OBJECT_TYPE_NPC               0x00000800
    COMBATLOG_OBJECT_TYPE_PLAYER            0x00000400
- Controller
    COMBATLOG_OBJECT_CONTROL_MASK           0x00000300
    COMBATLOG_OBJECT_CONTROL_NPC            0x00000200
    COMBATLOG_OBJECT_CONTROL_PLAYER         0x00000100
- Reaction
    COMBATLOG_OBJECT_REACTION_MASK          0x000000F0
    COMBATLOG_OBJECT_REACTION_HOSTILE       0x00000040
    COMBATLOG_OBJECT_REACTION_NEUTRAL       0x00000020
    COMBATLOG_OBJECT_REACTION_FRIENDLY      0x00000010
- Controller affiliation
    COMBATLOG_OBJECT_AFFILIATION_MASK       0x0000000F
    COMBATLOG_OBJECT_AFFILIATION_OUTSIDER   0x00000008
    COMBATLOG_OBJECT_AFFILIATION_RAID       0x00000004
    COMBATLOG_OBJECT_AFFILIATION_PARTY      0x00000002
    COMBATLOG_OBJECT_AFFILIATION_MINE       0x00000001
- Special cases (non-exclusive)
    COMBATLOG_OBJECT_SPECIAL_MASK           0xFFFF0000
    COMBATLOG_OBJECT_NONE                   0x80000000
    COMBATLOG_OBJECT_MAINASSIST             0x00080000
    COMBATLOG_OBJECT_MAINTANK               0x00040000
    COMBATLOG_OBJECT_FOCUS                  0x00020000
    COMBATLOG_OBJECT_TARGET                 0x00010000

================================== Raid Flag ==================================
    COMBATLOG_OBJECT_RAIDTARGET_MASK        0x000000FF
    COMBATLOG_OBJECT_RAIDTARGET8            0x00000080
    COMBATLOG_OBJECT_RAIDTARGET7            0x00000040
    COMBATLOG_OBJECT_RAIDTARGET6            0x00000020
    COMBATLOG_OBJECT_RAIDTARGET5            0x00000010
    COMBATLOG_OBJECT_RAIDTARGET4            0x00000008
    COMBATLOG_OBJECT_RAIDTARGET3            0x00000004
    COMBATLOG_OBJECT_RAIDTARGET2            0x00000002
    COMBATLOG_OBJECT_RAIDTARGET1            0x00000001
    
================================== Spell School ==================================
Type        Type
(bitmask)   (dec)   Name     Combination
00000001    1       Physical    #FFFF00 - 255, 255, 0
00000010    2       Holy        #FFE680 - 255, 230, 128
00000100    4       Fire        #FF8000 - 255, 128, 0
00001000    8       Nature      #4DFF4D - 77, 255, 77
00010000    16      Frost       #80FFFF - 128, 255, 255
00100000    32      Shadow      #8080FF - 128, 128, 255
01000000    64      Arcane      #FF80FF - 255, 128, 255
Double schools  
00000011    3       Holystrike Holy + Physical
00000101    5       Flamestrike Fire + Physical
00000110    6       Holyfire (Radiant) Fire + Holy
00001001    9       Stormstrike Nature + Physical
00001010    10      Holystorm Nature + Holy
00001100    12      Firestorm Nature + Fire
00010001    17      Froststrike Frost + Physical
00010010    18      Holyfrost Frost + Holy
00010100    20      Frostfire Frost + Fire
00011000    24      Froststorm Frost + Nature
00100001    33      Shadowstrike Shadow + Physical
00100010    34      Shadowlight (Twilight) Shadow + Holy
00100100    36      Shadowflame Shadow + Fire
00101000    40      Shadowstorm (Plague) Shadow + Nature
00110000    48      Shadowfrost Shadow + Frost
01000001    65      Spellstrike Arcane + Physical
01000010    66      Divine Arcane + Holy
01000100    68      Spellfire Arcane + Fire
01001000    72      Spellstorm (Astral) Arcane + Nature
01010000    80      Spellfrost Arcane + Frost
01100000    96      Spellshadow Arcane + Shadow
Triple and multi schools
00011100    28      Elemental Frost + Nature + Fire
01111100    124     Chromatic (Chaos) Arcane + Shadow + Frost + Nature + Fire
01111110    126     Magic Arcane + Shadow + Frost + Nature + Fire + Holy
01111111    127     Chaos Arcane + Shadow + Frost + Nature + Fire + Holy + Physical

================================== Power Type ==================================
Value   Type
-2      HealthCost 
-1      None 
0       Mana 
1       Rage 
2       Focus 
3       Energy
4       ComboPoints 
5       Runes 
6       RunicPower 
7       SoulShards 
8       LunarPower 
9       HolyPower 
10      Alternate 
11      Maelstrom 
12      Chi 
13      Insanity 
14      Obsolete 
15      Obsolete2 
16      ArcaneCharges 
17      Fury 
18      Pain 
19      NumPowerTypes

================================== Miss Type ==================================
- ABSORB
- BLOCK
- DEFLECT
- DODGE
- EVADE
- IMMUNE
- MISS
- PARRY
- REFLECT
- RESIST

================================== Aura Type ==================================
- BUFF
- DEBUFF

================================== Aura Type ==================================
- Drowning
- Falling
- Fatigue
- Fire
- Lava
- Slime

================================== Failed  Type ==================================
TODO Check up on that



"""