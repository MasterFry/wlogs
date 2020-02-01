#pragma once

#include "AGUIDUnitType.h"

class GUIDVignette : public AGUIDUnitType
{

protected:

  virtual ~GUIDVignette() = default;
  GUIDVignette(const GUIDVignette&) = delete;
  GUIDVignette &operator=(const GUIDVignette&) = delete;


public:

  GUIDVignette(WLogFileReader* reader) :
    AGUIDUnitType(GUIDType::VIGNETTE, reader)
  {
  }

};
