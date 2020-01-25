
from .Time import Time
from .Lua import parseLuaObject

        
class BuffLog:
    def __init__(self, time, buffs):
        self.time = Time(time.split('-'))
        self.buffs = buffs


class PlayerBuffs:
    def __init__(self):
        self.buffs = dict()

    def set(self, time, casterGUID, playerGUID, spellID):
        player = str(playerGUID)
        if player not in self.buffs:
            self.buffs[player] = dict()
        self.buffs[player][str(spellID)] = (time, str(casterGUID))

    def unset(self, time, playerGUID, spellID):
        player = str(playerGUID)
        if player not in self.buffs:
            return
        self.buffs[player][str(spellID)] = (time, None)

    def unsetAll(self, time, playerGUID):
        player = str(playerGUID)
        if player not in self.buffs:
            return
        for spellID in self.buffs[player]:
            self.buffs[player][spellID] = (time, None)

    def load(self, buffLog: BuffLog):
        for guid in buffLog.buffs:
            self.buffs[guid] = dict()
            for spellID in buffLog.buffs[guid]:
                self.buffs[guid][str(spellID)] = (buffLog.time, guid)

    @staticmethod
    def toLine(buffs):
        strings = list()
        for spellID in buffs:
            if buffs[spellID][1] is not None:
                strings.append(buffs[spellID][1] + ',' + spellID)
        return '[' + ','.join(strings) + ']'

    @staticmethod
    def merge(a, b):
        for spellID in b:
            if spellID not in a or a[spellID][0] < b[spellID][0]:
                a[spellID] = b[spellID]

    def copy(self, playerGUID):
        assert(playerGUID is not None)
        if playerGUID not in self.buffs:
            return dict()
        return dict(self.buffs[playerGUID])


class BuffLogFile:
    def __init__(self, fname):
        self.fname = fname
        self.buffLogs = list()
        self.index = 0
    
    def load(self):
        print('Loading from %s...' % self.fname)
        with open(self.fname) as file:
            # luaData = { Time : { GUID : [spellIDs..], GUID : [spellIDs..] , .. } , ..}
            name, luaData = parseLuaObject(file.read())
            assert(name == 'BuffLog_SavedBuffs')

            self.buffLogs = list()
            for time in luaData:
                self.buffLogs.append(BuffLog(time, luaData[time]))
            self.buffLogs.sort(key=lambda x: x.time)
        print('Done loading %s' % self.fname)

    def peek(self) -> BuffLog:
        if self.index >= len(self.buffLogs):
            return BuffLog('14-0-0-0-0', None)
        return self.buffLogs[self.index]

    def next(self) -> BuffLog:
        if self.index >= len(self.buffLogs):
            return None
        bufflog = self.buffLogs[self.index]
        self.index += 1
        return bufflog

    def reset(self):
        self.index = 0

    def merge(self, other):
        assert(False)