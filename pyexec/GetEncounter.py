#!/usr/bin/env python3

from wlog2 import WLog

wlog = WLog('cur/01_29_MC/Qopy.txt')
wlog.load()

# Onyxia group two is best

# Onygr
# Ouptw
# Oisbest

for i in range(len(wlog.encounters)):
    print(i, wlog.encounters[i].getName())

with open('magmadar.txt', 'w') as file:
    file.write(str(wlog.logVersion))
    file.write('\n')
    wlog.encounters[1].writeTo(file)
