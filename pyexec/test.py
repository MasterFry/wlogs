#!/usr/bin/env python3

# [Unit type]-0-[server ID]-[instance ID]-[zone UID]-[ID]-[spawn UID]
# [server ID]-[instance ID]-[zone UID] => equal for players in the same raid

from wlog2 import WLogParser
from wlog2 import Encoder
from wlog2.Encode import SizeType

count = [0] * len(SizeType)
sums = [0] * len(SizeType)

FILE_NAMES = [
    'cur/01_22_MC/Lesley.txt',
    'cur/01_27_Ony_Jette/Qopy.txt',
    'cur/01_27_Ony_Jexx/Lesley.txt'
]

for fname in FILE_NAMES:
    with WLogParser(fname) as parser:
        encoder = Encoder()
        while parser.hasNext():
            event = parser.getEvent()
            try:
                event.encode(encoder)
            except Exception:
                print(event)
                raise

        c, s = encoder.data()
        for i in range(len(c)):
            count[i] += c[i]
            sums[i] += s[i]

sizeTypeAvgs = [s / c for s, c in zip(sums, count)]
for i in range(len(sizeTypeAvgs)):
    print(SizeType(i).name, sizeTypeAvgs[i])
