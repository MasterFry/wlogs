#!/usr/bin/env python3
####################################################################################
#
#                           FOR MERGING / WRITING BUFFS
#
from os import listdir
from wlog2 import Merger
from wlog import endsWith

m = Merger()

for fname in listdir('cur/'):
    if endsWith(fname, '.txt'):
        m.addWLogFile('cur/' + fname)
    elif endsWith(fname, '.lua'):
        m.addBuffLogFile('cur/' + fname)

m.setOutputPath('merge.txt')
m.merge()
####################################################################################
