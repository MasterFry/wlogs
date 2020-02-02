from ..Time import Time

from ..guid import parseGUID
from ..types import EventType
from ..encode.AEncoder import AEncoder
from ..encode.ADecoder import ADecoder
from ..encode.SizeType import SizeType

from ..EventParser import EventParser

from .AEvent import AEvent

# 0 : Timestamp
#       1/22 20:39:53.422  
# 1 : Event Name
#       COMBATANT_INFO
# 2 : playerGUID
#       Player-4701-00F19EBB
# 3 : Strength
#       61
# 4 : Agility
#       75
# 5 : Stamina
#       337
# 6 : Intelligence
#       269
# 7 : Spirit
#       172
# 8 : Dodge
#       0 ==> static
# 9 : Parry
#       0 ==> static
# 10 : Block
#       0 ==> static
# 11: CritMelee
#       0 ==> static
# 12: CritRanged
#       0 ==> static
# 13: CritSpell
#       0 ==> static
# 14: Speed
#       0 ==> static
# 15: Lifesteal
#       0 ==> static
# 16: HasteMelee
#       0 ==> static
# 17: HasteRanged
#       0 ==> static
# 18: HasteSpell
#       0 ==> static
# 19: Avoidance
#       0 ==> static
# 20: Mastery
#       0 ==> static
# 21: VersatilityDamageDone
#       0 ==> static
# 22: VersatilityHealingDone
#       0 ==> static
# 23: VersatilityDamageTaken
#       0 ==> static
# 24: Armor
#       1657
# 25: CurrentSpecID
#       0 ==> static
# 26: (Class Talent 1, ...),
#       () ==> static
# 27: (PvP Talent 1, ...),
#       (0,0,0,0) ==> static
# 28: [Artifact Trait ID 1, Trait Effective Level 1, ...],
#       [] ==> static
# 29: [(Equipped Item ID 1,Equipped Item iLvL 1,(Permanent Enchant ID, Temp Enchant ID, On Use Spell Enchant ID),(Bonus List ID 1, ...),(Gem ID 1, Gem iLvL 1, ...)) ...],
#       [(10097,57,(),(),()),(18317,58,(),(),()),(10100,57,(),(),()),(4334,34,(),(),()),(14153,62,(),(),()),(11662,54,(),(),()),(16930,76,(),(),()),(18735,62,(911,0,0),(),()),(16804,66,(929,0,0),(),()),(18407,62,(930,0,0),(),()),(18103,63,(),(),()),(12543,60,(),(),()),(12930,60,(),(),()),(18467,62,(),(),()),(18350,61,(),(),()),(17103,71,(2504,0,0),(),()),(19309,65,(),(),()),(15279,51,(),(),()),(19032,20,(),(),())]
# 30: [Interesting Aura Caster GUID 1, Interesting Aura Spell ID 1, ...]
#       []

class EventCombatantInfo(AEvent):
    def __init__(self, time, parser):
        AEvent.__init__(self, time, EventType.COMBATANT_INFO)
        
        if isinstance(parser, EventParser):
            self.playerGUID = parser.getGUID()  # 2
            self.strength = parser.getInt()     # 3
            self.agility = parser.getInt()      # 4
            self.stamina = parser.getInt()      # 5
            self.intellect = parser.getInt()    # 6
            self.spirit = parser.getInt()       # 7
            assert(parser.readValue() == '0')   # 8
            assert(parser.readValue() == '0')   # 9
            assert(parser.readValue() == '0')   # 10
            assert(parser.readValue() == '0')   # 11
            assert(parser.readValue() == '0')   # 12
            assert(parser.readValue() == '0')   # 13
            assert(parser.readValue() == '0')   # 14
            assert(parser.readValue() == '0')   # 15
            assert(parser.readValue() == '0')   # 16
            assert(parser.readValue() == '0')   # 17
            assert(parser.readValue() == '0')   # 18
            assert(parser.readValue() == '0')   # 19
            assert(parser.readValue() == '0')   # 20
            assert(parser.readValue() == '0')   # 21
            assert(parser.readValue() == '0')   # 22
            assert(parser.readValue() == '0')   # 23
            self.armor = parser.getInt()        # 24 Can be negative apparently
            assert(parser.readValue() == '0')   # 25

            c = parser.getContainer()
            assert(len(c) == 0)
            c = parser.getContainer()
            assert(len(c) == 4)
            assert(c[0] == '0')
            assert(c[1] == '0')
            assert(c[2] == '0')
            assert(c[3] == '0')
            c = parser.getContainer()
            assert(len(c) == 0)

            self.gear = ','.join(parser.getContainer())

            buffs = parser.getContainer() # = [GUID,spellId,GUID,spellId,...]
            self.buffs = dict() # = { spellId: (time, srcGUID), ..}
            for i in range(0, len(buffs), 2):
                guid = parseGUID(buffs[i])
                spellId = int(buffs[i + 1])
                self.buffs[spellId] = (self.time, guid)

            # remains = parser.readValue(delim='\n') # 26 - 30
            # assert(remains[:16] == '(),(0,0,0,0),[],')
            # assert(remains[-2:] == '[]') # TODO
            # self.gear = remains[16:-3]          # 29
            # self.buffs = dict() # = { spellId: (time, srcGUID), ..}
            
        elif isinstance(parser, ADecoder):
            self.decode(decode)
        else:
            ValueError('Parser not supported: ' + type(parser))


    def decode(self, decoder: ADecoder):
        self.playerGUID = decoder.guid()
        self.strength = decoder.integer(size=SizeType.COMBATANT_STATS)
        self.agility = decoder.integer(size=SizeType.COMBATANT_STATS)
        self.stamina = decoder.integer(size=SizeType.COMBATANT_STATS)
        self.intellect = decoder.integer(size=SizeType.COMBATANT_STATS)
        self.spirit = decoder.integer(size=SizeType.COMBATANT_STATS)
        self.armor = decoder.integer(size=SizeType.COMBATANT_STATS, signed=True)
        self.gear = decoder.string()
        
        self.buffs = dict()
        buffCount = decoder.integer(size=SizeType.BUFF_COUNT)
        for _ in range(buffCount):
            guid = decoder.guid()
            spellId = decoder.integer(size=SizeType.SPELL_ID)
            self.buffs[spellId] = (Time.MIN(), guid)
        
    def encode(self, encoder: AEncoder) -> bytes:
        buffs = encoder.integer(len(self.buffs), size=SizeType.BUFF_COUNT)
        for spellId in self.buffs:
            buffs += encoder.guid(self.buffs[spellId][1]) + encoder.integer(spellId, size=SizeType.SPELL_ID)

        # TODO gear
        return AEvent.encode(self, encoder) + \
               encoder.guid(self.playerGUID) + \
               encoder.integer(self.strength, size=SizeType.COMBATANT_STATS) + \
               encoder.integer(self.agility, size=SizeType.COMBATANT_STATS) + \
               encoder.integer(self.stamina, size=SizeType.COMBATANT_STATS) + \
               encoder.integer(self.intellect, size=SizeType.COMBATANT_STATS) + \
               encoder.integer(self.spirit, size=SizeType.COMBATANT_STATS) + \
               encoder.integer(self.armor, size=SizeType.COMBATANT_STATS, signed=True) + \
               encoder.string(self.gear) + \
               buffs

    def mergeBuffs(self, other):
        assert(isinstance(other, EventCombatantInfo))
        for spellId in other.buffs:
            if spellId not in self.buffs or \
               self.buffs[spellId][0] < other.buffs[spellId][0]:
                self.buffs[spellId] = other.buffs[spellId]

    def __str__(self):
        return AEvent.__str__(self) + \
            ',{0:s},{1:d},{2:d},{3:d},{4:d},{5:d},0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,{6:d},0,(),(0,0,0,0),[],[{7:s}],[{8:s}]'.format(
                str(self.playerGUID),
                self.strength,
                self.agility,
                self.stamina,
                self.intellect,
                self.spirit,
                self.armor,
                self.gear,
                # ','.join(['{0:s},{1:d}'.format('0000000000000000', spellId) for spellId in self.buffs])
                ','.join(['{0:s},{1:d}'.format(str(self.playerGUID), spellId) for spellId in self.buffs])
                # ','.join(['{0:s},{1:d}'.format(str(self.buffs[spellId][1]), spellId) for spellId in self.buffs])
            )

    def __eq__(self, other):
        return AEvent.__eq__(self, other) and \
               self.strength == other.strength and \
               self.agility == other.agility and \
               self.stamina == other.stamina and \
               self.intellect == other.intellect and \
               self.spirit == other.spirit and \
               self.armor == other.armor and \
               self.gear == other.gear

    def __ne__(self, other):
        return not self.__eq__(other)
