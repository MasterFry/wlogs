from os.path import exists
from os.path import isdir
from time import process_time

from .WLogFile import WLogFile
from .Buffs import BuffLogFile

class Merger:
    def __init__(self):
        self.wLogFiles = list()
        self.buffLogFiles = list()
        self.outPath = './merge.txt'

    def addWLogFile(self, file: str):
        Merger.checkFile(file)
        self.wLogFiles.append(file)

    def addWLogFiles(self, files: list):
        for file in files:
            self.addWLogFile(file)

    def addBuffLogFile(self, file: str):
        Merger.checkFile(file)
        self.buffLogFiles.append(file)

    def addBuffLogFiles(self, files: list):
        for file in files:
            self.addBuffLogFiles(file)

    def setOutputPath(self, outPath):
        self.outPath = outPath

    def merge(self):
        buffLog = None
        if len(self.buffLogFiles) > 0:
            buffLogs = [BuffLogFile(x) for x in self.buffLogFiles]
            for buffLog in buffLogs:
                buffLog.load()

            # Merge all the BuffLogFiles together, resulting in one list of BuffLogs
            buffLog = buffLogs[0]
            for i in range(1, len(buffLogs)):
                buffLog.merge(buffLogs[i])
        
        wLogs = [WLogFile(x) for x in self.wLogFiles]
        for wLog in wLogs:
            if buffLog is not None:
                wLog.setBuffLogFile(buffLog)
            wLog.load()
        
        if len(self.wLogFiles) > 0:
            # Merge all the WLogFiles together
            wLog = wLogs[0]
            print(self.wLogFiles[0], 'X')
            for i in range(1, len(wLogs)):
                print('X', self.wLogFiles[i])
                start = process_time()
                wLog.merge(wLogs[i])
                end = process_time()
                print(end - start, 's') # seconds

        wLog.save(self.outPath)

    @staticmethod
    def checkFile(fname: str):
        if not isinstance(fname, str):
            raise ValueError('The file path must be given as a string')
        if not exists(fname):
            raise ValueError('File does not exist: %s' % fname)
        if isdir(fname):
            raise ValueError('File is a directory: %s' % fname)

