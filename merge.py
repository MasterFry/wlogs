#!/usr/bin/env python3
####################################################################################
#
#                           FOR MERGING / WRITING BUFFS
#
from os import listdir
from wlog2 import Merger
from wlog import endsWith

m = Merger()

# m.addWLogFile('cur/End_Game_24_2_BWL_1.txt')
DIR = 'cur/02_26_BWL/'
for fname in listdir(DIR):
    if endsWith(fname, '.txt'):
        m.addWLogFile(DIR + fname)
    elif endsWith(fname, '.lua'):
        m.addBuffLogFile(DIR + fname)

m.setOutputPath('merge.txt')
m.merge()
####################################################################################
