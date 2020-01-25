#!/usr/bin/env python3
####################################################################################
#
#                           FOR MERGING / WRITING BUFFS
#
from os import listdir
from wlog import Merger

m = Merger()
m.addWLogFile('cur/Qopy.txt')
m.addWLogFile('cur/Lesley.txt')
m.addBuffLogFile('cur/BuffLog.lua')
m.setOutputPath('merge.txt')
m.merge()
####################################################################################
