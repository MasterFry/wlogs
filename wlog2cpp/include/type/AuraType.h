#pragma once

#include "TypeUtils.h"

namespace types
{
  
  extern const char* AURA_TYPE_NAMES[];

  enum class AuraType : unsigned char
  {
    BUFF = 0,
    DEBUFF = 1
  };

  inline const char* getCName(AuraType type)
  {
    return AURA_TYPE_NAMES[(size_t) type];
  }

  inline string_t getName(AuraType type)
  {
    return std::string(getCName(type));
  }

  inline AuraType getAuraType(string_t name)
  {
    return (AuraType) findNameInArray(name, AURA_TYPE_NAMES, AURA_TYPE_NAMES_COUNT);
  }

};
