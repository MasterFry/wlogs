#pragma once

#include "AGUID.h"
#include "../io/WLogFileReader.h"

class GUIDNull : public AGUID
{

protected:

  virtual ~GUIDNull() = default;
  GUIDNull(const GUIDNull&) = delete;
  GUIDNull &operator=(const GUIDNull&) = delete;

public:

  GUIDNull(WLogFileReader* reader) :
    AGUID(GUIDType::NIL)
  {
  }

  void write(FILE* file) override;

};

inline void GUIDNull::write(FILE* file)
{
  fputs("0000000000000000", file);
}
