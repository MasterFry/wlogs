#!/usr/bin/env python3

from wlog2.WLogParser import WLogParser
from wlog2.types import EventType, getEventName

covered = set()

print('COPYING...')
with open('cur/copy.txt', 'w') as file:
    with WLogParser('cur/Qopy.txt') as parser:
        while parser.hasNext():
            event = parser.getEvent()
            covered.add(event.eventType)
            file.write(str(event))
            file.write('\n')

print('COMPARING...')
with open('cur/copy.txt') as copy:
    with open('cur/Qopy.txt') as orig:
        copyLine = copy.readline()
        origLine = orig.readline()
        count = 1
        while copyLine != '' or origLine != '':
            if copyLine != origLine:
                print('COPY:')
                print(copyLine)
                print('ORIGINAL:')
                print(origLine)
                print('DIFFERENCE DETECTED AT LINE: %d' % count)
                exit(0)
            copyLine = copy.readline()
            origLine = orig.readline()
            count += 1

print('DONE')

print('NOT COVERED EVENT TYPES:')
for i in range(0, 50):
    if EventType(i) not in covered:
        print(getEventName(EventType(i)))

# NOT COVERED EVENT TYPES:
# DAMAGE_SPLIT
# ENCHANT_APPLIED
# ENCHANT_REMOVED
# SPELL_PERIODIC_DRAIN
# SPELL_PERIODIC_LEECH
# UNIT_DESTROYED
# UNIT_DISSIPATES
# UNIT_LOYALTY