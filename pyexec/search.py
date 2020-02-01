#!/usr/bin/env python3

import sys

from wlog import endsWith
from wlog import WLogFile
from wlog import Event


# KEYWORDS = ['UNIT_DIED', 'Lesley']
# # KEYWORDS = ['ENCOUNTER_END']

# file = WLogFile('cur/Lesley.txt')
# file.load()

# def bits(val: int) -> str:
#     b = ''
#     while val > 0:
#         b += '0' if (val & 1) == 0 else '1'
#         val = val >> 1
#     return b[::-1]

# r = list()
# r1 = list()
# r2 = list()
# d = dict()
# ex = dict()

# r1 = [1000] * 4
# r2 = [0] * 4

# for enc in file.encounters:
#     for e in enc.events:
#         if endsWith(e.event, '_ENERGIZE'):
#             assert(len(e.params) == 4)
#             for i in range(2):
#                 p = float(e.params[i])
#                 if p < r1[i]:
#                     r1[i] = p
#                 if p > r2[i]:
#                     r2[i] = p
            
#             if e.params[2] not in r:
#                 r.append(e.params[2])
            
#             p = int(e.params[3])
#             if p < r1[3]:
#                 r1[3] = p
#             if p > r2[3]:
#                 r2[3] = p
            


# print(r)
# print(r1)
# print(r2)
# print(d)
# print(ex)

# with open('cur/Lesley.txt') as file:
#     line = file.readline()
#     while line != '':
#         if all([key in line for key in KEYWORDS]):
#             sys.stdout.write(line)

#         line = file.readline()

# 1/22 21:51:34.112  SPELL_DAMAGE,Player-4701-00B48D7F,"Qopy-Mograine",0x511,0x0,Creature-0-4469-409-26884-11502-000028B529,"Ragnaros",0x10a48,0x0,10181,"Frostbolt",0x10,Creature-0-4469-409-26884-11502-000028B529,0000000000000000,1,100,0,0,0,-1,0,0,0,838.31,-831.47,0,4.1757,63,
# 1819,827,-1,16,0,0,0,1,nil,nil
# 1/22 21:34:05.556  SPELL_DAMAGE,Player-4701-00B48D7F,"Qopy-Mograine",0x511,0x0,Creature-0-4469-409-26884-11988-000028A101,"Golemagg the Incinerator",0x10a48,0x0,10181,"Frostbolt",0x10,Creature-0-4469-409-26884-11988-000028A101,0000000000000000,33,100,0,0,0,-1,0,0,0,830.97,-1005.79,0,1.6202,63,
# 919,835,-1,16,0,0,0,nil,nil,nil
# 1/22 20:50:57.820  SWING_DAMAGE,Player-4701-012FB28F,"Redcheat-Mograine",0x514,0x0,Creature-0-4469-409-26884-11502-000028B529,"Ragnaros",0xa48,0x0,Player-4701-012FB28F,0000000000000000,100,100,0,0,0,-1,0,0,0,847.94,-815.61,0,4.0742,66,
# 252,292,-1,1,0,0,0,nil,1,nil

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