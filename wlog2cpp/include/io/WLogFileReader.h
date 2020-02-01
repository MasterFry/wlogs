#pragma once

#include "types.h"
#include "StringBuilder.h"
#include "time.h"

#include <cstdio>

#define READER_BUFFER_SIZE 4096
#define READER_STRING_BUFFER_CAPACITY 512

using namespace types;

class AGUID;

class WLogFileReader
{

protected:

  WLogFileReader(const WLogFileReader&) = delete;
  WLogFileReader &operator=(const WLogFileReader&) = delete;

  string_t fileName;
  FILE* file;
  char buffer[READER_BUFFER_SIZE];
  size_t bufferIndex;
  size_t bufferSize;
  StringBuilder builder;

  void read();
  
public:
  WLogFileReader(string_t fileName = "") :
    fileName(fileName),
    file(nullptr),
    bufferIndex(0),
    bufferSize(0),
    builder(READER_STRING_BUFFER_CAPACITY)
  {
  }

  ~WLogFileReader()
  {
    if(file != nullptr)
      close();
  }

  void open(string_t fileName);
  void open();
  void close();
  
  bool hasNext();
  char getChar();

  string_t readValue(char delim = ',');
  ssize_t readSigned(char delim = ',');
  size_t readUnsigned(char delim = ',', size_t base = 10);
  float readFloat(char delim = ',');
  string_t readString();

  AuraType readAuraType();
  EnvironmentalType readEnvironmentalType();
  EventType readEventType();
  GUIDType readGUIDType();
  MissType readMissType();

  AGUID* readGUID();
  time_t readTime();

// container

};

inline void WLogFileReader::read()
{
  bufferSize = fread((void*) buffer, 1, READER_BUFFER_SIZE, file);
  bufferIndex = 0;
}

inline void WLogFileReader::open()
{
  open(fileName);
}

inline void WLogFileReader::open(string_t fileName)
{
  file = fopen(fileName.c_str(), "r");
  read();
}

inline void WLogFileReader::close()
{
  fclose(file);
  file = nullptr;
}

inline bool WLogFileReader::hasNext()
{
  return bufferIndex < bufferSize;
}

inline char WLogFileReader::getChar()
{
  if(unlikely(bufferIndex == bufferSize))
    read();
  return buffer[bufferIndex++];
}

inline AuraType WLogFileReader::readAuraType()
{
  return getAuraType(readValue());
}

inline EnvironmentalType WLogFileReader::readEnvironmentalType()
{
  return getEnvironmentalType(readValue());
}

inline EventType WLogFileReader::readEventType()
{
  return getEventType(readValue());
}

inline MissType WLogFileReader::readMissType()
{
  return getMissType(readValue());
}
