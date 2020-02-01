#!/usr/bin/env python3

from wlog import startsWith, endsWith
import re

AP_TEMPLATE = '''{{

protected:

  {0:s}(EventType type, WLogFileReader* reader) :
    {1:s}(type, reader)
  {{
    assert(false);
  }}

  virtual ~{0:s}() = default;
  {0:s}(const {0:s}&) = delete;
  {0:s} &operator=(const {0:s}&) = delete;

public:

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

}};

inline bool {0:s}::operator==(const AEvent& other)
{{
  assert(false);
}}

inline bool {0:s}::operator!=(const AEvent& other)
{{
  assert(false);
}}

inline void {0:s}::write(FILE* file)
{{
  fprintf(file, "", this);
}}

'''

A_TEMPLATE = '''{{

protected:

  {0:s}(EventType type, WLogFileReader* reader) :
  {{
    assert(false);
  }}

  virtual ~{0:s}() = default;
  {0:s}(const {0:s}&) = delete;
  {0:s} &operator=(const {0:s}&) = delete;

public:

  virtual bool operator==(const AEvent& other);
  virtual bool operator!=(const AEvent& other);

  virtual void write(FILE* file);

}};

inline bool {0:s}::operator==(const AEvent& other)
{{
  assert(false);
}}

inline bool {0:s}::operator!=(const AEvent& other)
{{
  assert(false);
}}

inline void {0:s}::write(FILE* file)
{{
  fprintf(file, "", this);
}}

'''

TEMPLATE = '''{{

public:

  {0:s}(WLogFileReader* reader) :
    {1:s}(EventType, reader)
  {{
    assert(false);
  }}

  virtual ~{0:s}() = default;
  {0:s}(const {0:s}&) = delete;
  {0:s} &operator=(const {0:s}&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

}};

inline bool {0:s}::operator==(const AEvent& other)
{{
  assert(false);
}}

inline bool {0:s}::operator!=(const AEvent& other)
{{
  assert(false);
}}

inline void {0:s}::write(FILE* file)
{{
  fprintf(file, "", this);
}}

'''

def convert(name):
    infos = list()
    parents = list()

    lines = None
    with open('wlog2/event/%s.py' % name) as file:
        lines = file.readlines()
    assert(lines is not None)

    for line in lines:
        if line.strip() == '\n':
            continue

        elif startsWith(line, 'from'):
            continue

        elif startsWith(line, '#'):
            infos.append(line[1:])

        elif startsWith(line, 'class'):
            b = line.index('(')
            e = line.index(')')
            assert(name == line[6:b])
            parents = [x.strip() for x in line[b + 1 : e].split(',')]
            if 'ABC' in parents:
                assert(len(parents) == 1)
                parents = list()
    
            break

    with open('wlog2cpp/include/event/%s.h' % name, 'w') as file:
        print('writing %s ...' % name)
        file.write('#pragma once\n\n')
        for parent in parents:
            file.write('#include "%s.h"\n' % parent)
        if len(parents) == 0:
            file.write('#include "EventType.h"\n')
            file.write('\n')
            file.write('#include <cstdio>\n')
        file.write('\n')
        file.write('using namespace types;\n')
        file.write('\n')
        for info in infos:
            file.write('//%s' % info)
        file.write('\n')
        file.write('class %s' % name)
        if len(parents) > 0:
            file.write(' : public %s' % parents[0])
            for i in range(1, len(parents)):
                file.write(', public %s' % parents[i])
        file.write('\n')
        if name[0] == 'A':
            if len(parents) == 0:
                file.write(A_TEMPLATE.format(name))
            else:
                file.write(AP_TEMPLATE.format(name, parents[0]))
        else:
            file.write(TEMPLATE.format(name, parents[0]))

            
from os import listdir

for name in listdir('wlog2/event/'):
    if name == '__init__.py':
        continue
    convert(name[:-3])
        