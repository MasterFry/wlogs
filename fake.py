#!/usr/bin/env python3

from wlog import WLogFile
from wlog import Event

s = '"Doncarleon-Mograine"'
print(s)
print(s.lstrip('"').split('-')[0])

# file = WLogFile('cur/Qopy.txt')
# file.load()

# guid = file.findGUID('Qopy')
