from abc import ABC
from abc import abstractmethod

from .types import *

from .Time import Time


class EventParsingError(Exception):
    def __init__(self, message=''):
        Exception.__init__(self, message)


class EventParser(ABC):
    def __init__(self, fname):
        self.fname = fname
        self.file = None
        self.buffer = None
        self.bufferIndex = 0
        self.lineNumber = 0

    def open(self, fname) -> None:
        self.fname = fname
        self.file = open(fname)
        self.buffer = ''
        self.bufferIndex = 0
        self.lineNumber = 0

    def close(self) -> None:
        self.file.close()
        self.fname = None
        self.file = None
        self.buffer = None

    def getChar(self) -> str:
        if len(self.buffer) <= self.bufferIndex:
            self.buffer = self.file.readline()
            self.lineNumber += 1
            self.bufferIndex = 0
        
        c = self.buffer[self.bufferIndex]
        self.bufferIndex += 1
        return c

    def hasNext(self) -> bool:
        if len(self.buffer) <= self.bufferIndex:
            self.buffer = self.file.readline()
            self.lineNumber += 1
            self.bufferIndex = 0
        return len(self.buffer) > self.bufferIndex

    def peekValue(self, delim=',') -> str:
        value = ''
        index = self.bufferIndex
        
        while self.buffer[index] != delim and self.buffer[index] != '\n':
            value += self.buffer[index]
            index += 1
        
        return value

    def readValue(self, delim=',') -> str:
        value = ''
        c = self.getChar()
        while c != delim and c != '\n':
            value += c
            c = self.getChar()
        return value

    def getAuraType(self) -> AuraType:
        value = self.readValue()
        try:
            index = AURA_TYPE_NAMES.index(value)
            return AuraType(index)
        except ValueError:
            raise EventParsingError('Invalid Aura Type: ' + value)

    def getMissType(self) -> MissType:
        value = self.readValue()
        try:
            index = MISS_TYPE_NAMES.index(value)
            return MissType(index)
        except ValueError:
            raise EventParsingError('Invalid Miss Type: ' + value)

    def getEnvironmentalType(self) -> EnvironmentalType:
        value = self.readValue()
        try:
            index = ENVIRONMENTAIL_TYPE_NAMES.index(value)
            return EnvironmentalType(index)
        except ValueError:
            raise EventParsingError('Invalid Environmental Type: ' + value)

    def getTime(self) -> Time:
        # "1/22 20:51:35.210  "
        params = list()
        params.append(self.readValue(delim='/'))
        params.append(self.readValue(delim=' '))
        params.append(self.readValue(delim=':'))
        params.append(self.readValue(delim=':'))
        params.append(self.readValue(delim=' '))
        # month  = self.readValue(delim='/')
        # day    = self.readValue(delim=' ')
        # hour   = self.readValue(delim=':')
        # minute = self.readValue(delim=':')
        # second = self.readValue(delim=' ')
        if self.getChar() != ' ':
            raise EventParsingError('No double space after Time!')

        return Time(params)

    def getEventType(self) -> EventType:
        name = self.readValue()
        index = EVENT_NAMES.index(name)
        if index == -1:
            raise EventParsingError('Invalid Event Type: ' + name)
        
        return EventType(index)

    def getInt(self, delim=',', base=10, nullable=False) -> int:
        value = self.readValue(delim=delim)
        if nullable and value == 'nil':
            return None
        return int(value, base=base)

    def getFloat(self, nullable=False) -> float:
        value = self.readValue()
        if nullable and value == 'nil':
            return None
        return float(value)

    def getString(self) -> str:
        value = self.getChar()
        if value == '"':
            value = self.readValue(delim='"')
            self.getChar()
            return value
        value += self.readValue(delim=',')
        if value == 'nil':
            return None
        raise EventParsingError('Invalid String value: ' + value)

    def getContainer(self) -> list:
        elements = list()
        layer = list()

        c = self.getChar()
        if c != '(' and c != '[' and c != '{':
            raise EventParsingError('Container must start with ( , [ or { .')
        layer.append(c)

        CONT_START = ['(', '[', '{']
        CONT_END = { ')': '(', ']': '[', '}': '{' }
        element = ''
        c = self.getChar()
        while c != '\n' and c != '':
            if c == ',' and len(layer) == 0:
                break

            if c == ',' and len(layer) == 1:
                elements.append(element)
                element = ''
            elif c in CONT_START:
                layer.append(c)
                element += c
            elif c in CONT_END:
                if layer.pop() != CONT_END[c]:
                    raise EventParsingError('Container inconsistency!')
                if len(layer) > 0:
                    element += c
            else:
                element += c
            
            c = self.getChar()
        
        if element != '':
            elements.append(element)
        
        return elements

    @abstractmethod
    def getGUID(self):
        pass
        # value = self.readValue()
        # return GUID(value)  
