
class LuaObjectError(Exception):
    def __init__(self, msg: str, index: int, data: str):
        if index + 50 < len(data):
            super(LuaObjectError, self).__init__('%s at index: %d, data: %s...' % (msg, index, data[index : index + 50]))
        else:
            super(LuaObjectError, self).__init__('%s at index: %d, data: %s' % (msg, index, data[index:]))


def parseLuaObjectsFromFile(fname: str):
    file = open(fname)
    objects = parseLuaObjects(file.read())
    file.close()
    return objects


def parseLuaObjects(data: str):
    parser = LuaObjectParser()
    return parser.parse(data)


def toLuaString(data: dict):
    writer = LuaObjectWriter()
    return writer.write(data)


def saveAsLuaString(data: dict, fname: str):
    with open(fname, 'w') as file:
        file.write(toLuaString(data))


class LuaObjectParser:
    def __init__(self):
        self.INT_TERMINATORS = [',', '}', ']']
        self.data = None
        self.index = 0

    def parse(self, data):
        objects = dict()
        self.data = LuaObjectParser.strip(data)

        self.index = 0
        while self.index < len(self.data):
            nameIndex = self.index
            self.index = self.data.find('=', self.index)
            name = self.data[nameIndex : self.index]
            self.index += 1
            objects[name] = self.readValue()

        self.data = None
        return objects

    def readValue(self):
        if self.index + 2 < len(self.data) and self.data[self.index : self.index + 3] == 'nil':
            self.index += 3
            return None
        if self.data[self.index] == '{':
            self.index += 1
            if self.data[self.index] == '[':
                return self.readDict()
            else:
                return self.readList()
        elif self.data[self.index] == '"':
            self.index += 1
            return self.readString()
        else:
            return self.readInteger()

    def readList(self):
        value = list()

        while self.index < len(self.data):
            if self.data[self.index] == '}':
                self.index += 1
                break
            
            value.append(self.readValue())

            if self.data[self.index] == ',':
                self.index += 1

        return value
    
    def readDict(self):
        value = dict()

        while self.index < len(self.data):
            if self.data[self.index] == '}':
                self.index += 1
                break

            if self.data[self.index] != '[':
                raise LuaObjectError('Excpected [', self.index, self.data)
            self.index += 1
            # if self.data[self.index : self.index + 2] != '["':
            #     raise LuaObjectError('Excpected ["', self.index, self.data)
            # self.index += 2

            key = self.readValue()
            # key = self.readString()

            if self.data[self.index : self.index + 2] != ']=':
                raise LuaObjectError('Excpected ]=', self.index, self.data)
            self.index += 2
                
            value[key] = self.readValue()

            if self.data[self.index] == ',':
                self.index += 1
        
        return value

    def readString(self):
        begin = self.index
        while self.index < len(self.data):
            if self.data[self.index] == '"' and self.data[self.index - 1] != '\\':
                break
            self.index += 1
        if self.data[self.index] != '"':
            raise LuaObjectError('Excpected "', self.index, self.data)
        self.index += 1
        return self.data[begin : self.index - 1]

    def readInteger(self):
        begin = self.index
        while self.index < len(self.data):
            if self.data[self.index] in self.INT_TERMINATORS:
                break
            self.index += 1
        try:
            return int(self.data[begin : self.index])
        except ValueError as ex:
            raise LuaObjectError('Invalid Integer', self.index, self.data)

    @staticmethod
    def strip(data: str) -> str:
        string = False
        comment = False
        multiComment = False
        newData = ''

        for i in range(len(data)):
            if multiComment:
                if data[i - 1 : i + 1] == ']]':
                    multiComment = False
                continue
            if comment:
                if data[i] == '\n':
                    comment = False
                continue
            if data[i] == '"':
                string = not string
            elif not string:
                if i + 1 < len(data) and data[i : i + 2] == '--':
                    if i + 3 < len(data) and data[i + 2 : i + 4] == '[[':
                        multiComment = True
                    else:
                        comment = True
                    continue
                if data[i] == ' '  or \
                   data[i] == '\t' or \
                   data[i] == '\n' or \
                   data[i] == '\r':
                    continue
            newData += data[i]

        return newData


class LuaObjectWriter:
    def __init__(self):
        self.indent = ''
        self.lua = ''

    def increaseIndent(self):
        self.indent += '\t'

    def decreaseIndent(self):
        assert(len(self.indent) > 0)
        self.indent = self.indent[:-1]

    def write(self, data: dict):
        for name in data:
            self.lua += name + ' = '
            self.writeValue(data[name])
            self.lua += '\n'
        return self.lua

    def writeValue(self, value):
        if isinstance(value, dict):
            self.lua += '{\n'
            self.increaseIndent()
            for key in value:
                self.lua += self.indent + '['
                self.writeValue(key)
                self.lua += '] = '
                self.writeValue(value[key])
                self.lua += ',\n'
            self.decreaseIndent()
            self.lua += self.indent + '}'

        elif isinstance(value, list):
            self.lua += '{\n'
            self.increaseIndent()
            for val in value:
                self.writeValue(value[key])
                self.lua += ',\n'
            self.decreaseIndent()
            self.lua += self.indent + '}'

        elif isinstance(value, int):
            self.lua += str(value)

        elif isinstance(value, str):
            self.lua += '"' + value + '"'

        elif value is None:
            self.lua += 'nil'

        else:
            assert(False)
