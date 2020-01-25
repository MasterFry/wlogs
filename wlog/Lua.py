
class LuaObjectError(Exception):
    pass


def parseLuaObject(data):
    parser = LuaObjectParser()
    return parser.parse(data)


class LuaObjectParser:
    def __init__(self):
        self.data = None
        self.index = 0

    def parse(self, data):
        self.data = LuaObjectParser.strip(data)
        self.index = self.data.find('=')
        name = self.data[:self.index]
        self.index += 1
        value = self.readValue()
        self.data = None
        return name, value

    def readValue(self):
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

            if self.data[self.index : self.index + 2] != '["':
                raise LuaObjectError
            self.index += 2

            key = self.readString()

            if self.data[self.index : self.index + 2] != ']=':
                raise LuaObjectError
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
            raise LuaObjectError
        self.index += 1
        return self.data[begin : self.index - 1]

    def readInteger(self):
        begin = self.index
        while self.index < len(self.data):
            if self.data[self.index] == ',' or self.data[self.index] == '}':
                break
            self.index += 1
        return int(self.data[begin : self.index])

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
