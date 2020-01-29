from enum import IntEnum

class SizeType(IntEnum):
    ALTERNATE_POWER_TYPE  = 0
    AURA_AMOUNT           = 1
    COMBATANT_STATS       = 2
    COMBATLOG_PROJECT_ID  = 3
    COMBATLOG_VERSION     = 4
    COORDINATE            = 5
    DIFFICULTY_ID         = 6
    DAMAGE_AMOUNT         = 7
    DAMAGE_P2             = 8
    DAMAGE_P3             = 9
    ENCOUNTER_ID          = 10
    ENCOUNTER_START_P4    = 11
    ENERGIZE_AMOUNT       = 12
    EXTRA_ATTACK_AMOUNT   = 13
    FACING                = 14
    FLAGS                 = 15
    HEAL_AMOUNT           = 16
    HEAL_P1               = 17
    HP                    = 18
    ITEM_ID               = 19
    LEVEL                 = 20
    MISSED_AMOUNT         = 21
    MISSED_CRITICAL       = 22
    PLAYER_COUNT          = 23
    BUFF_COUNT            = 24
    POWER_TYPE            = 25
    RAID_FLAGS            = 26
    SPELL_ABSORBED_AMOUNT = 27
    SPELL_ABSORBED_P5     = 28
    SPELL_ID              = 29
    SPELL_SCHOOL          = 30
    MAP_ID                = 31
    TYPE_EVENT            = 32
    TYPE_ENVIRONMENT      = 33
    TYPE_AURA             = 34
    TYPE_MISS             = 35
    TYPE_GUID             = 36
    GUID_ID               = 37
    GUID_SERVER_ID        = 38
    GUID_INSTANCE_ID      = 39
    GUID_ZONE_UID         = 40
    GUID_SPAWN_UID        = 41
    GUID_ITEM_SPAWN_UID   = 42
    GUID_PLAYER_UID       = 43
    DRAIN_AMOUNT          = 44
    DRAIN_P6              = 45

SIZE_TYPE_VALUES = [
    1, #        ALTERNATE_POWER_TYPE  
    1, #        AURA_AMOUNT           
    1, #        COMBATANT_STATS       
    1, # 1-S    COMBATLOG_PROJECT_ID  
    1, # 1-S    COMBATLOG_VERSION     
    1, #        COORDINATE            
    1, # 1-S    DIFFICULTY_ID         
    1, #        DAMAGE_AMOUNT         
    1, #        DAMAGE_P2             
    1, #        DAMAGE_P3             
    1, #        ENCOUNTER_ID          
    1, #        ENCOUNTER_START_P4    
    1, #        ENERGIZE_AMOUNT       
    1, #        EXTRA_ATTACK_AMOUNT   
    1, #        FACING                
    1, # 4      FLAGS                 
    1, #        HEAL_AMOUNT           
    1, #        HEAL_P1               
    1, # 1-S    HP                    
    1, #        ITEM_ID               
    1, # 1-S    LEVEL                 
    1, #        MISSED_AMOUNT         
    1, #        MISSED_CRITICAL       
    1, # 1-S    PLAYER_COUNT
    1, # 1-S    BUFF_COUNT          
    1, #        POWER_TYPE            
    1, # 4      RAID_FLAGS            
    1, #        SPELL_ABSORBED_AMOUNT 
    1, #        SPELL_ABSORBED_P5     
    1, #        SPELL_ID              
    1, # 1-S    SPELL_SCHOOL          
    1, #        MAP_ID                
    1, # 1-S    TYPE_EVENT            
    1, # 1-S    TYPE_ENVIRONMENT      
    1, # 1-S    TYPE_AURA             
    1, # 1-S    TYPE_MISS             
    1, # 1-S    TYPE_GUID             
    1, #        GUID_ID               
    1, #        GUID_SERVER_ID        
    1, #        GUID_INSTANCE_ID      
    1, #        GUID_ZONE_UID         
    1, # 5-S    GUID_SPAWN_UID        
    1, # 8-S    GUID_ITEM_SPAWN_UID        
    1, # 4-S    GUID_PLAYER_UID       
    1, #        DRAIN_AMOUNT          
    1  #        DRAIN_P6              
]
