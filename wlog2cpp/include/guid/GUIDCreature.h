#pragma once

#include "AGUIDUnitType.h"

class GUIDCreature : public AGUIDUnitType
{

protected:

  virtual ~GUIDCreature() = default;
  GUIDCreature(const GUIDCreature&) = delete;
  GUIDCreature &operator=(const GUIDCreature&) = delete;


public:

  GUIDCreature(WLogFileReader* reader) :
    AGUIDUnitType(GUIDType::CREATURE, reader)
  {
  }

};
