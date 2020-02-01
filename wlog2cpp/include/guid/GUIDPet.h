#pragma once

#include "AGUIDUnitType.h"

class GUIDPet : public AGUIDUnitType
{

protected:

  virtual ~GUIDPet() = default;
  GUIDPet(const GUIDPet&) = delete;
  GUIDPet &operator=(const GUIDPet&) = delete;


public:

  GUIDPet(WLogFileReader* reader) :
    AGUIDUnitType(GUIDType::PET, reader)
  {
  }

};
