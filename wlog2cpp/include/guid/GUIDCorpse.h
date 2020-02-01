#pragma once

#include "AGUIDUnitType.h"

class GUIDCorpse : public AGUIDUnitType
{

protected:

  virtual ~GUIDCorpse() = default;
  GUIDCorpse(const GUIDCorpse&) = delete;
  GUIDCorpse &operator=(const GUIDCorpse&) = delete;


public:

  GUIDCorpse(WLogFileReader* reader) :
    AGUIDUnitType(GUIDType::CORPSE, reader)
  {
  }

};
