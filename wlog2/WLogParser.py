from .EventParser import *
from .event import *
from .guid import *

class WLogParser(EventParser):
    def __init__(self, fname=None):
        EventParser.__init__(self, fname)

    def __enter__(self):
        self.open(self.fname)
        return self

    def __exit__(self, ex_type, ex_value, ex_traceback):
        if ex_type is not None:
            if self.buffer is not None:
                print('At line %d: %s' % (self.lineNumber, self.buffer))
            raise
        self.close()

    def getEvent(self) -> AEvent:
        time = self.getTime()
        eventType = self.getEventType()
        return EVENT_TABLE[getEventName(eventType)](time, self)

    def getGUID(self) -> AGUID:
        value = self.getChar()
        if value == '0':
            value += self.readValue(delim=',')
        else:
            value += self.readValue(delim='-')
        return GUID_TABLE[value](self)
