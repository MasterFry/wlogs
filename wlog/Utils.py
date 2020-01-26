

class CorruptionError(Exception):
    pass


class AdvancedLoggingError(Exception):
    def __init__(self):
        super().__init__('Advanced Combat Logging must be enabled!')


def wlog_split_line(line: str) -> list:
    delimiters = [' ', ',', '/', ':', '"', '\n']
    elements = list()
    current = ''
    string = False

    for c in line:
        if c in delimiters:
            if string:
                if c == '"':
                    assert(current != '')
                    elements.append(current + '"')
                    current = ''
                    string = False
                else:
                    current += c
            elif c == '"':
                assert(current == '')
                current = '"'
                string = True
            else:
                if current != '':
                    elements.append(current)
                current = ''
        else:
            current += c

    assert(current == '')#

    return elements


def startsWith(string, start):
    return len(string) >= len(start) and string[:len(start)] == start


def endsWith(string, end):
    return len(string) >= len(end) and string[-len(end):] == end