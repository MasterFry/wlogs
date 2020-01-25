from .GUID import GUID
from .Time import Time
from .Utils import endsWith

from .Constants import PARAM_COUNT
from .Constants import PREFIX_PARAM_COUNT

from .Encoding import EventType
from .Encoding import getEventName
from .Encoding import getEventType
from .Encoding import Encoder
from .Encoding import encodeDynamic

import struct

class Event:
    def __init__(self, params):
        # check params
        if len(params) < 14:
            print(params)
            print(len(params))
            assert(False)

        # save all the base params
        self.time          = Time(params)
        self.event         = params[5]
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


def __encode(event: Event) -> bytes:
    encoder = Encoder()
    eventType = getEventType(event.event)

    src = encoder.entity(event.srcGUID, event.srcName, event.srcFlags, event.srcRaidFlags)
    dest = encoder.entity(event.destGUID, event.destName, event.destFlags, event.destRaidFlags)
    code = event.time.encode() + int(eventType).to_bytes(1, byteorder='little') + src + dest

    if eventType == EventType.DAMAGE_SHIELD or \
       eventType == EventType.DAMAGE_SHIELD_MISSED or \
       eventType == EventType.DAMAGE_SPLIT or \
       eventType == EventType.ENCHANT_APPLIED or \
       eventType == EventType.ENCHANT_REMOVED or \
       eventType == EventType.RANGE or \
       eventType == EventType.SPELL:
        code += encoder.spell(event.prefix_params[0], event.prefix_params[1], event.prefix_params[2])

    if event.has_advanced_params:
        unit = encoder.guid(event.unitGUID)
        owner = encoder.guid(event.ownerGUID)
        currHp = event.currHp.to_bytes(1, byteorder='little')
        assert(event.maxHp == '100')
        assert(event.attackPower == '0')
        assert(event.spellPower == '0')
        assert(event.armor == '0')
        assert(event.resourceType == '-1')
        assert(event.currResource == '0')
        assert(event.maxResource == '0')
        assert(event.resourceCost == '0')
        coord1 = struct.pack('<f', event.coord_1)
        coord2 = struct.pack('<f', event.coord_2)
        assert(event.UiMapID == '0')
        facing = struct.pack('<f', event.facing)
        level = event.currHp.to_bytes(1, byteorder='little')
        code += unit + owner + currHp + coord1 + coord2 + facing + level
        # struct.calcsize('f')

    if eventType == EventType.SPELL_DURABILITY_DAMAGE:
        code += encoder.item(params[0], params[1])

    elif endsWith(event.event, '_DAMAGE'):
        i = 0
        if eventType == EventType.ENVIRONMENTAL_DAMAGE:
            # environmentalType
            code += encoder.environmentalType(params[0])
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
        amount    = encodeDynamic(event.params[i + 0], size=2)
        val1      = encodeDynamic(event.params[i + 1], size=2)
        val2      = encodeDynamic(event.params[i + 2], size=2)
        school    = encodeDynamic(event.params[i + 3], size=1)
        resisted  = encodeDynamic(event.params[i + 4], size=2)
        blocked   = encodeDynamic(event.params[i + 5], size=2)
        absorbed  = encodeDynamic(event.params[i + 6], size=2)
        flags     = encodeFlags(event.params[i + 7:])
        code += amount + val1 + val2 + school + resisted + blocked + absorbed + flags

    elif endsWith(event.event, '_MISSED'):
        # missType, isOffHand, amountMissed, critical
        pass

    elif endsWith(event.event, '_HEAL'):
        # amount, overhealing, absorbed, critical
        assert(event.param[0] == event.param[1])
        amount      = encodeDynamic(event.params[1], size=2)
        overhealing = encodeDynamic(event.params[2], size=2)
        absorbed    = encodeDynamic(event.params[3], size=2)
        critical    = encodeFlags(list(event.params[4]))
        code += amount + overhealing + absorbed + critical
    
    elif endsWith(event.event, '_ENERGIZE'):
        # amount, overEnergize, powerType, alternatePowerType
        pass
    
    elif endsWith(event.event, '_DRAIN') or \
         endsWith(event.event, '_LEECH'):
        # amount, powerType, extraAmount
        pass
    
    elif endsWith(event.event, '_INTERRUPT'):
        # extraSpellId, extraSpellName, extraSchool
        code += encoder.spell(event.params[0], event.params[1], event.params[2])

    elif endsWith(event.event, '_DISPEL'):
        # extraSpellId, extraSpellName, extraSchool, auraType
        code += encoder.spell(event.params[0], event.params[1], event.params[2])
        code += encoder.auraType(event.params[3])

    elif endsWith(event.event, '_DISPEL_FAILED'):
        # extraSpellId, extraSpellName, extraSchool
        code += encoder.spell(event.params[0], event.params[1], event.params[2])

    elif endsWith(event.event, '_STOLEN'):
        # extraSpellId, extraSpellName, extraSchool, auraType
        code += encoder.spell(event.params[0], event.params[1], event.params[2])
        code += encoder.auraType(event.params[3])

    elif endsWith(event.event, '_EXTRA_ATTACKS'):
        # amount
        code += encodeDynamic(int(event.params[0]), size=2)

    elif endsWith(event.event, '_AURA_APPLIED')      or \
         endsWith(event.event, '_AURA_REMOVED')      or \
         endsWith(event.event, '_AURA_APPLIED_DOSE') or \
         endsWith(event.event, '_AURA_REMOVED_DOSE') or \
         endsWith(event.event, '_AURA_REFRESH'):
        # auraType, amount
        code += encoder.auraType(event.params[0])
        code += encodeDynamic(int(event.params[1]), size=2)

    elif endsWith(event.event, '_AURA_BROKEN'):
        # auraType
        code += encoder.auraType(event.params[0])

    elif endsWith(event.event, '_AURA_BROKEN_SPELL'):
        # extraSpellId, extraSpellName, extraSchool, auraType
        code += encoder.spell(event.params[0], event.params[1], event.params[2])
        code += encoder.auraType(event.params[3])

    elif endsWith(event.event, '_CAST_FAILED'):
        # failedType
        pass

    elif endsWith(event.event, '_ABSORBED '):
        # amount
        code += encodeDynamic(int(event.params[1]), size=2)

    else:
        assert(len(event.params) == 0 and 'Parameters were not handled')
    

# 1/22 21:49:44.038  SPELL_DURABILITY_DAMAGE,
# Creature-0-4469-409-26884-11502-000028B529,"Ragnaros",0x10a48,0x0,
# Player-4701-009A42DA,"Jettesnell-Mograine",0x514,0x0,
# 21388,"Melt Weapon",0x4,
# 17071,"Gutgore Ripper"