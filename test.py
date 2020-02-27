#!/usr/bin/env python3

from os import listdir
from os.path import isdir
from wlog import endsWith

def search(fname):
    print('searching %s...' % fname)
    with open(fname) as file:
        for line in file.readlines():
            if 'ENCHANT_APPLIED' in line or 'ENCHANT_REMOVED' in line:
                print('\t%s' % line[:-1])

def findLog(dir, func):
    if dir[-1] != '/':
        dir += '/'
    for fname in listdir(dir):
        if isdir(dir + fname):
            findLog(dir + fname, func)
        elif endsWith(fname, '.txt'):
            func(dir + fname)

findLog('cur', search)
