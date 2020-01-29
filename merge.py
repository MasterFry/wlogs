#!/usr/bin/env python3
####################################################################################
#
#                           FOR MERGING / WRITING BUFFS
#
from os import listdir
from wlog import Merger
from wlog import endsWith

m = Merger()

DIR = 'cur/01_27_Ony_Jexx/'
for fname in listdir(DIR):
    if endsWith(fname, '.txt'):
        m.addWLogFile(DIR + fname)
    elif endsWith(fname, '.lua'):
        m.addBuffLogFile(DIR + fname)

m.setOutputPath('merge_v1.txt')
m.merge()
####################################################################################
