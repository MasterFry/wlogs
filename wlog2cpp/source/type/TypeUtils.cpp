#include "TypeUtils.h"

#include <stdexcept>

int types::findNameInArray(string_t name, const char* array[], size_t length)
{
  for(size_t i = 0; i < length; ++i)
  {
    if(name.compare(array[i]) == 0)
      return i;
  }
  throw std::invalid_argument("Invalid Name: " + name);
}
