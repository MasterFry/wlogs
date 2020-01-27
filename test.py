#!/usr/bin/env python3

from wlog2.WLogParser import WLogParser

events = list()

with open('cur/copy.txt', 'w') as file:
    with WLogParser('cur/Qopy.txt') as parser:
        file.write(str(parser.getEvent()))
        file.write('\n')
