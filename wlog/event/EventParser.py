from .Event import Event

from .EventType import EventType
from .EventType import EVENT_NAMES
from .AuraType import AuraType

from ..GUID import GUID
from ..Time import Time


class EventParsingError(Exception):
    def __init__(self, message=''):
        Exception.__init__(self, message)


class EventParser:
    def __init__(self, fname=None):
        self.fname = fname
        self.file = None

    def open(self, fname) -> None:
        self.fname = fname
        self.file = open(fname)

    def close(self) -> None:
        self.file.close()
        self.fname = None
        self.file = None

    def __enter__(self):
        self.open(self.fname)

    def __exit__(self, ex_type, ex_value, ex_traceback):
        if ex_type is not None:
            raise
        self.close()

    def readValue(self, delim=',') -> str:
        value = ''
        c = self.file.read(1)
        while c != delim and c != '\n' and c != '':
            value += c
            c = self.file.read(1)
        return value

    def getAuraType(self) -> AuraType:
        value = self.readValue()
        if value == 'BUFF':
            return AuraType.BUFF
        if value == 'DEBUFF':
            return AuraType.DEBUFF
        raise EventParsingError('Invalid AuraType: ' + value)

    def getTime(self) -> Time:
        # "1/22 20:51:35.210  "
        month  = self.readValue(delim='/')
        day    = self.readValue(delim=' ')
        hour   = self.readValue(delim=':')
        minute = self.readValue(delim=':')
        second = self.readValue(delim=' ')
        if self.file.read(1) != ' ':
            raise EventParsingError('No double space after Time!')

        return Time(list(month, day, hour, minute, second))

    def getEventType(self) -> EventType:
        name = self.readValue()
        index = EVENT_NAMES.index(name)
        if index == -1:
            raise EventParsingError('Invalid Event Type: ' + name)
        
        return EventType(index)

    def getInt(self, base=10, nullable=False) -> int:
        value = self.readValue()
        if nullable and value == 'nil':
            return None
        return int(value, base=base)

    def getFloat(self, nullable=False) -> float:
        value = self.readValue()
        if nullable and value == 'nil':
            return None
        return float(value)

    def getString(self, nullable=False) -> str:
        value = self.readValue()
        if nullable and value == 'nil':
            return None
        if value[0] != '"' or value[-1] != '"':
            raise EventParsingError('Invalid String value: ' + value)
        return value[1:-1]

    def getGUID(self) -> GUID:
        value = self.readValue()
        return GUID(value)

    def getEvent(self) -> Event:
        time = self.getTime()
        eventType = self.getEventType()

        
