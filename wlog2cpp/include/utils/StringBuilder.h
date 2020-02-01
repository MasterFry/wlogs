#pragma once

#include "std.h"

#include <string>
#include <stdexcept>

class StringBuilder
{

protected:

  size_t capacity;
  size_t size;
  char* buffer;

public:

  StringBuilder(size_t capacity) :
    capacity(capacity),
    size(0),
    buffer(new char[capacity])
  {
    if(buffer == nullptr)
      throw std::bad_alloc();
  }

  virtual ~StringBuilder()
  {
    if(buffer != nullptr)
      delete[] buffer;
  }
  
  StringBuilder(const StringBuilder&) = delete;
  StringBuilder &operator=(const StringBuilder&) = delete;

  void put(char c);
  std::string getString();

};

inline void StringBuilder::put(char c)
{
  if(likely(size < capacity))
    buffer[size++] = c;
  throw std::out_of_range("StringBuffer is full!");
}

inline std::string StringBuilder::getString()
{
  auto value = std::string(buffer, size);
  size = 0;
  return value;
}
