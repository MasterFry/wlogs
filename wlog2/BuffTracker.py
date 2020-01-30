from wlog import parseLuaObjects
from .Time import Time

from .guid import *
from .types import *

from .UnitFlag import UnitFlag

class BuffLog:
    def __init__(self, time, buffs):
        self.time = time
        self.buffs = buffs # = { GUID : [spellIDs..], GUID : [spellIDs..] , .. }


class BuffTracker:
    def __init__(self):
        # Structure:
        # buffs = { destGUID: { spellId: (time, srcGUID), ..}, ..}
        # GUID's as strings!
        self.buffs = dict()
        self.buffLogs = list()
        self.buffLogIndex = 0

    def reset(self):
        self.buffs = dict()
        self.buffLogIndex = 0

    def getBuffs(self, playerGUID):
        playerGUID = str(playerGUID)
        buffs = dict()
        
        if playerGUID in self.buffs:
            for spellId in self.buffs[playerGUID]:
                if self.buffs[playerGUID][spellId][1] is not None:
                    buffs[spellId] = self.buffs[playerGUID][spellId]
        
        return buffs

    def checkEvent(self, event):
        if UnitFlag.isOutsider(event.destFlags) or not UnitFlag.isPlayer(event.destFlags):
            return

        if event.eventType == EventType.SPELL_AURA_APPLIED or \
           event.eventType == EventType.SPELL_AURA_APPLIED_DOSE or \
           event.eventType == EventType.SPELL_AURA_REFRESH:
            self.setBuff(event.time, event.srcGUID, event.destGUID, event.spellId)

        elif event.eventType == EventType.SPELL_AURA_BROKEN or \
             event.eventType == EventType.SPELL_AURA_BROKEN_SPELL or \
             event.eventType == EventType.SPELL_AURA_REMOVED or \
             event.eventType == EventType.SPELL_AURA_REMOVED_DOSE:
            self.unsetBuff(event.time, event.srcGUID, event.spellId)

        elif event.eventType == EventType.UNIT_DIED or \
             event.eventType == EventType.SPELL_INSTAKILL:
            self.unsetAllBuffs(event.time, event.destGUID)

    def setBuff(self, time, srcGUID, destGUID, spellId):
        assert(srcGUID is None or isinstance(srcGUID, AGUID))
        if self.nextBuffLogTime() < time:
            self.setNextBuffLog()
        destGUID = str(destGUID)
        # if spellId == 17538:
        #     print('MONGOOSE at %s on %s from %s.' % (str(time), str(destGUID), str(srcGUID)))
        if destGUID not in self.buffs:
            self.buffs[destGUID] = dict()
        self.buffs[destGUID][spellId] = (time, srcGUID)

    def unsetBuff(self, time, destGUID, spellId):
        if self.nextBuffLogTime() < time:
            self.setNextBuffLog()
        self.setBuff(time, None, destGUID, spellId)

    def unsetAllBuffs(self, time, destGUID):
        if self.nextBuffLogTime() < time:
            self.setNextBuffLog()
        destGUID = str(destGUID)
        if destGUID in self.buffs:
            for spellId in self.buffs[destGUID]:
                self.buffs[destGUID][spellId] = (time, None)
    
    def loadBuffLog(self, fname: str):
        print('Loading from %s...' % fname)
        with open(fname) as file:
            # luaData = { Time : { GUID : [spellIDs..], GUID : [spellIDs..] , .. } , ..}
            luaData = parseLuaObjects(file.read())
            assert('BuffLog_SavedBuffs' in luaData)
            luaData = luaData['BuffLog_SavedBuffs']

            for key in luaData:
                time = Time(key.split('-'))
                buffLog = BuffLog(time, luaData[key])
                self.buffLogs.append(buffLog)

        self.buffLogs.sort(key=lambda x: x.time)
        print('Done loading %s.' % fname)

    def nextBuffLogTime(self) -> Time:
        if self.buffLogIndex < len(self.buffLogs):
            return self.buffLogs[self.buffLogIndex].time
        return Time.MAX()

    def setNextBuffLog(self):
        assert(self.buffLogIndex < len(self.buffLogs))
        
        time = self.buffLogs[self.buffLogIndex].time
        buffs = self.buffLogs[self.buffLogIndex].buffs
        for guidKey in buffs:
            guid = parseGUID(guidKey)
            self.buffs[guidKey] = dict()
            for spellId in buffs[guidKey]:
                self.buffs[guidKey][spellId] = (time, guid)
        
        self.buffLogIndex += 1
