from .GUID import GUID
from .Time import Time
from .Utils import endsWith

from .Constants import PARAM_COUNT
from .Constants import PREFIX_PARAM_COUNT


class Event:
    def __init__(self, params):
        if len(params) < 6:
            print(params)
            print(len(params))
            assert(False)

        self.time  = Time(params)
        self.event = params[5]

        if self.event == 'COMBAT_LOG_VERSION':
            self.version = int(params[6])
            assert(params[7] == 'ADVANCED_LOG_ENABLED')
            self.advancedLogEnabled = params[8] == '1'
            assert(params[9] == 'BUILD_VERSION')
            self.build = params[10]
            assert(params[11] == 'PROJECT_ID')
            self.projectId = params[11]
            return
        
        if self.event == 'ENCOUNTER_START':
            self.encounterId = int(params[6])
            self.encounterName = params[7]
            self.difficultyId = int(params[8])
            self.groupSize = int(params[9])
            self.p10 = params[10] # TODO find out
            return
            
        if self.event == 'ENCOUNTER_END':
            self.encounterId = int(params[6])
            self.encounterName = params[7]
            self.difficultyId = int(params[8])
            self.groupSize = int(params[9])
            self.success = params[10] == '1'
            return

        if self.event == 'COMBATANT_INFO':
            self.buffs = None
            return

        # check params
        if len(params) < 14 and params[5] not in ['COMBAT_LOG_VERSION', 'ENCOUNTER_START', 'ENCOUNTER_END', 'COMBATANT_INFO']:
            print(params)
            print(len(params))
            assert(False)

        # save all the remaining base params
        self.srcGUID       = GUID(params[6])
        self.srcName       = params[7]
        self.srcFlags      = int(params[8], 16)
        self.srcRaidFlags  = params[9]
        self.destGUID      = GUID(params[10])
        self.destName      = params[11]
        self.destFlags     = int(params[12], 16)
        self.destRaidFlags = params[13]

        # Check if the event is listed
        if not self.event in PARAM_COUNT:
            print(params)
            print(len(params))
        assert(self.event in PARAM_COUNT)

        # determine the prefix param count
        prefix_param_count = -1
        for prefix in PREFIX_PARAM_COUNT:
            if self.event.startswith(prefix):
                prefix_param_count = PREFIX_PARAM_COUNT[prefix]
                break
        # check if a prefix param count for the event is listed
        if prefix_param_count == -1:
            print(params)
            print(len(params))
        assert(prefix_param_count != -1)
        
        # save the prefix params
        index = 14 + prefix_param_count
        self.prefix_params = list()
        for i in range(14, index):
            if PARAM_COUNT[self.event] <= i:
                print(params)
                print(prefix_param_count)
            self.prefix_params.append(params[i])
        
        # save the advanced params if present
        # 31 = 5 timestamp + 9 base + 16 advanced
        self.has_advanced_params = PARAM_COUNT[self.event] >= 31
        if self.has_advanced_params:
            # fake advanced params if not present
            self.unitGUID     = GUID(params[index + 0])
            self.ownerGUID    = GUID(params[index + 1])
            self.currHp       = params[index + 2]
            self.maxHp        = params[index + 3]
            self.attackPower  = params[index + 4]
            self.spellPower   = params[index + 5]
            self.armor        = params[index + 6]
            self.resourceType = params[index + 7]
            self.currResource = params[index + 8]
            self.maxResource  = params[index + 9]
            self.resourceCost = params[index + 10]
            self.coord_1      = float(params[index + 11]) # adjust => use avg when merging
            self.coord_2      = float(params[index + 12]) # adjust => use avg when merging
            self.UiMapID      = params[index + 13]
            self.facing       = params[index + 14] # adjust
            self.level        = params[index + 15]
            index += 16
        
        # save any params left
        self.params = params[index:]
    
    def __str__(self):
        params = [
            self.event,
            str(self.srcGUID),
            self.srcName,
            '%#x' % self.srcFlags,
            self.srcRaidFlags,
            str(self.destGUID),
            self.destName,
            '%#x' % self.destFlags,
            self.destRaidFlags
        ]
        
        params += self.prefix_params

        if self.has_advanced_params:
            params += [
                str(self.unitGUID),
                str(self.ownerGUID),
                self.currHp,
                self.maxHp,
                self.attackPower,
                self.spellPower,
                self.armor,
                self.resourceType,
                self.currResource,
                self.maxResource,
                self.resourceCost,
                '%.02f' % self.coord_1,
                '%.02f' % self.coord_2,
                self.UiMapID,
                self.facing,
                self.level      
            ]
        return str(self.time) + '  ' + ','.join(params + self.params)

    def __eq__(self, other):
        if not isinstance(other, Event):
            return False
        if len(self.prefix_params) != len(other.prefix_params) or \
           len(self.params) != len(other.params):
            return False
        # if self.time != other.time:
        #     return False
        for i in range(len(self.prefix_params)):
            if self.prefix_params[i] != other.prefix_params[i]:
                return False
                
        if len(self.params) > 0 and self.params[0] != other.params[0]:
            return False # only spellID needs to be compared
        # for i in range(len(self.params)):
        #     if self.params[i] != other.params[i]:
        #         return False

        if self.event         != other.event         or \
           self.srcGUID       != other.srcGUID       or \
           self.destGUID      != other.destGUID      :
            return False
        #    self.srcName       != other.srcName       or \
        #    self.srcRaidFlags  != other.srcRaidFlags  or \
        #    self.destName      != other.destName      or \
        #    self.destRaidFlags != other.destRaidFlags :
        #    self.srcFlags      != other.srcFlags      or \
        #    self.destFlags     != other.destFlags     or \
        if self.has_advanced_params:
            if self.unitGUID     != self.unitGUID     or \
               self.ownerGUID    != self.ownerGUID    :
                return False
            #    self.currHp       != self.currHp       or \
            #    self.maxHp        != self.maxHp        or \
            #    self.attackPower  != self.attackPower  or \
            #    self.spellPower   != self.spellPower   or \
            #    self.armor        != self.armor        or \
            #    self.resourceType != self.resourceType or \
            #    self.currResource != self.currResource or \
            #    self.maxResource  != self.maxResource  or \
            #    self.resourceCost != self.resourceCost or \
            #    self.UiMapID      != self.UiMapID      or \
            #    self.level        != self.level        :
            #    self.coord_1      != self.coord_1      or \
            #    self.coord_2      != self.coord_2      or \
            #    self.facing       != self.facing       or \
        return True
    
    def __ne__(self, other):
        return not self.__eq__(other)


# 5 : COMBATANT_INFO
# 6 : playerGUID
# 7 : Strength
# 8 : Agility
# 9 : Stamina
# 10: Intelligence
# 11: Dodge
# 12: Parry
# 13: Block
# 14: CritMelee
# 15: CritRanged
# 16: CritSpell
# 17: Speed
# 18: Lifesteal
# 19: HasteMelee
# 20: HasteRanged
# 21: HasteSpell
# 22: Avoidance
# 23: Mastery
# 24: VersatilityDamageDone
# 25: VersatilityHealingDone
# 26: VersatilityDamageTaken
# 27: Armor
# 28: CurrentSpecID
# 29: (Class Talent 1, ...),
#       <empty> ()
# 30: (PvP Talent 1, ...),
#       <empty> (0,0,0,0)
# 31: [Artifact Trait ID 1, Trait Effective Level 1, ...],
#       <empty> []
# 32: [(Equipped Item ID 1,Equipped Item iLvL 1,(Permanent Enchant ID, Temp Enchant ID, On Use Spell Enchant ID),(Bonus List ID 1, ...),(Gem ID 1, Gem iLvL 1, ...)) ...],
# 33: [Interesting Aura Caster GUID 1, Interesting Aura Spell ID 1, ...]
#       <empty> []