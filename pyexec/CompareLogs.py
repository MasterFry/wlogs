#!/usr/bin/env python3

count = 0
with open('merge_v1.txt') as file1:
    with open('merge_v2.txt') as file2:
        line1 = file1.readline()
        line2 = file2.readline()
        count += 1
        while line1 != '' and line2 != '':
            if 'COMBATANT_INFO' not in line1 or 'COMBATANT_INFO' not in line2:
                if (line1[:14] != line2[:14] or line1[17:] != line2[17:]) and count not in EXCEPT:
                    print('At Line: %d' % count)
                    print('V1:')
                    print(line1)
                    print('V2:')
                    print(line2)
                    assert(False)
            line1 = file1.readline()
            line2 = file2.readline()
            count += 1

# V1:
# 1/27 19:35:26.263  SPELL_ABSORBED,Creature-0-4469-249-14129-11262-0008AF3B60,"Onyxian Whelp",0xa48,0x0,Player-4701-0088B68B,"Lesley-Mograine",0x511,0x0,Player-4701-0088B68B,"Lesley-Mograine",0x511,0x0,13033,"Ice Barrier",0x10,306,387
# 1/27 19:35:26.263  SWING_DAMAGE_LANDED,Creature-0-4469-249-14129-11262-0008AF3B60,"Onyxian Whelp",0xa48,0x0,Player-4701-0088B68B,"Lesley-Mograine",0x511,0x0,Player-4701-0088B68B,0000000000000000,100,100,0,0,0,-1,0,0,0,-17.57,-193.48,0,6.2714,64,0,387,-1,1,0,0,306,nil,nil,nil

# V2:
# 1/27 19:35:26.263  SWING_DAMAGE_LANDED,Creature-0-4469-249-14129-11262-0008AF3B60,"Onyxian Whelp",0xa48,0x0,Player-4701-0088B68B,"Lesley-Mograine",0x511,0x0,Player-4701-0088B68B,0000000000000000,100,100,0,0,0,-1,0,0,0,-17.57,-193.48,0,6.2714,64,0,387,-1,1,0,0,306,nil,nil,nil
# 1/27 19:35:26.263  SPELL_ABSORBED,Creature-0-4469-249-14129-11262-0005AF3B60,"Onyxian Whelp",0xa48,0x0,Player-4701-0088B68B,"Lesley-Mograine",0x511,0x0,Player-4701-0088B68B,"Lesley-Mograine",0x511,0x0,13033,"Ice Barrier",0x10,340,430
