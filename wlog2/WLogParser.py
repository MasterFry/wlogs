from .EventParser import *
from .event import *

class WLogParser(EventParser):
    def __init__(self, fname=None):
        self.fname = fname
        self.file = None

    def __enter__(self):
        self.open(self.fname)
        return self

    def __exit__(self, ex_type, ex_value, ex_traceback):
        if ex_type is not None:
            raise
        self.close()

    def getEvent(self) -> AEvent:
        time = self.getTime()
        eventType = self.getEventType()
        return EVENT_TABLE[getEventName(eventType)](time, self)    
