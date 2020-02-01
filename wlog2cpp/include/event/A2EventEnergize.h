#pragma once

#include "EventType.h"

#include <cstdio>

using namespace types;

// 36.0000,0.0000,0,8319
//  1:  amount
//  2:  overEnergize
//  3:  powerType
//  4:  alternatePowerType

class A2EventEnergize
{

protected:

  A2EventEnergize(EventType type, WLogFileReader* reader) :
  {
    assert(false);
  }

  virtual ~A2EventEnergize() = default;
  A2EventEnergize(const A2EventEnergize&) = delete;
  A2EventEnergize &operator=(const A2EventEnergize&) = delete;

public:

  virtual bool operator==(const AEvent& other);
  virtual bool operator!=(const AEvent& other);

  virtual void write(FILE* file);

};

inline bool A2EventEnergize::operator==(const AEvent& other)
{
  assert(false);
}

inline bool A2EventEnergize::operator!=(const AEvent& other)
{
  assert(false);
}

inline void A2EventEnergize::write(FILE* file)
{
  fprintf(file, "", this);
}

