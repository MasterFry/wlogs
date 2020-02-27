from os.path import exists
from os.path import isdir
from time import process_time

from wlog import endsWith

from .WLog import WLog
from .BuffTracker import BuffTracker

class Merger:
    def __init__(self):
        self.wLogFiles = list()
        self.buffLogFiles = list()
        self.outPath = './merge.txt'

    def addWLogFile(self, file: str):
        Merger.checkWLogFile(file)
        self.wLogFiles.append(file)

    def addWLogFiles(self, files: list):
        for file in files:
            self.addWLogFile(file)

    def addBuffLogFile(self, file: str):
        Merger.checkBuffLogFile(file)
        self.buffLogFiles.append(file)

    def addBuffLogFiles(self, files: list):
        for file in files:
            self.addBuffLogFiles(file)

    def setOutputPath(self, outPath):
        Merger.checkOutputFile(outPath)
        self.outPath = outPath

    def merge(self):
        buffTracker = BuffTracker()
        for fname in self.buffLogFiles:
            buffTracker.loadBuffLog(fname)
        
        wLogs = [WLog(x) for x in self.wLogFiles]
        for wLog in wLogs:
            buffTracker.reset()
            wLog.load(buffTracker)

        if len(wLogs) == 0:
            print('No WLog Files set!')
            return
        
        # Merge all the WLogFiles together
        wLog = wLogs[0]
        for i in range(1, len(wLogs)):
            start = process_time()
            wLog.merge(wLogs[i])
            end = process_time()
            print('[WLOG]: Merge time: %.03f s' % (end - start))

        wLog.save(self.outPath)

    @staticmethod
    def checkWLogFile(fname: str):
        if not isinstance(fname, str):
            raise ValueError('The file path must be given as a string')
        if not endsWith(fname, '.txt'):
            raise ValueError('Invalid file format: %s' % fname)
        if not exists(fname):
            raise ValueError('File does not exist: %s' % fname)
        if isdir(fname):
            raise ValueError('File is a directory: %s' % fname)
        
    @staticmethod
    def checkBuffLogFile(fname: str):
        if not isinstance(fname, str):
            raise ValueError('The file path must be given as a string')
        if not endsWith(fname, '.lua'):
            raise ValueError('Invalid file format: %s' % fname)
        if not exists(fname):
            raise ValueError('File does not exist: %s' % fname)
        if isdir(fname):
            raise ValueError('File is a directory: %s' % fname)

    @staticmethod
    def checkOutputFile(fname: str):
        if not isinstance(fname, str):
            raise ValueError('The file path must be given as a string')
        if not endsWith(fname, '.txt'):
            raise ValueError('Invalid file format: %s' % fname)
        if exists(fname) and isdir(fname):
            raise ValueError('File is a directory: %s' % fname)
