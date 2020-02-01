#pragma once

#include "TypeUtils.h"

namespace types
{
  
  extern const char* GUID_TYPE_NAMES[];

  enum class GUIDType : unsigned char
  {
    NIL         = 0,
    PLAYER      = 1,
    CREATURE    = 2,
    PET         = 3,
    GAME_OBJECT = 4,
    VEHICLE     = 5,
    VIGNETTE    = 6,
    ITEM        = 7,
    CORPSE      = 8
  };

  inline const char* getCName(GUIDType type)
  {
    return GUID_TYPE_NAMES[(size_t) type];
  }

  inline string_t getName(GUIDType type)
  {
    return std::string(getCName(type));
  }

  inline GUIDType getGUIDType(string_t name)
  {
    return (GUIDType) findNameInArray(name, GUID_TYPE_NAMES, GUID_TYPE_NAMES_COUNT);
  }

};
