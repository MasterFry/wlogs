#pragma once

#include "TypeUtils.h"

namespace types
{
  
  extern const char* ENVIRONMENTAIL_TYPE_NAMES[];

  enum class EnvironmentalType : unsigned char
  {
    DROWNING = 0,
    FALLING = 1,
    FATIGUE = 2,
    FIRE = 3,
    LAVA = 4,
    SLIM = 5
  };

  inline const char* getCName(EnvironmentalType type)
  {
    return ENVIRONMENTAIL_TYPE_NAMES[(size_t) type];
  }

  inline string_t getName(EnvironmentalType type)
  {
    return std::string(getCName(type));
  }

  inline EnvironmentalType getEnvironmentalType(string_t name)
  {
    return (EnvironmentalType) findNameInArray(name, ENVIRONMENTAIL_TYPE_NAMES, ENVIRONMENTAIL_TYPE_NAMES_COUNT);
  }

};
