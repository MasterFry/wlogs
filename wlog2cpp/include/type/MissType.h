#pragma once

#include "TypeUtils.h"

namespace types
{
  
  extern const char* MISS_TYPE_NAMES[];

  enum class MissType : unsigned char
  {
    ABSORB  = 0,
    BLOCK   = 1,
    DEFLECT = 2,
    DODGE   = 3,
    EVADE   = 4,
    IMMUNE  = 5,
    MISS    = 6,
    PARRY   = 7,
    REFLECT = 8,
    RESIST  = 9
  };

  inline const char* getCName(MissType type)
  {
    return MISS_TYPE_NAMES[(size_t) type];
  }

  inline string_t getName(MissType type)
  {
    return std::string(getCName(type));
  }

  inline MissType getMissType(string_t name)
  {
    return (MissType) findNameInArray(name, MISS_TYPE_NAMES, MISS_TYPE_NAMES_COUNT);
  }

};
