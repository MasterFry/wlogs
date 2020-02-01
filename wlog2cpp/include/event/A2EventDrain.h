#pragma once

#include "EventType.h"

#include <cstdio>

using namespace types;

// amount, powerType, extraAmount ?

class A2EventDrain
{

protected:

  A2EventDrain(EventType type, WLogFileReader* reader) :
  {
    assert(false);
  }

  virtual ~A2EventDrain() = default;
  A2EventDrain(const A2EventDrain&) = delete;
  A2EventDrain &operator=(const A2EventDrain&) = delete;

public:

  virtual bool operator==(const AEvent& other);
  virtual bool operator!=(const AEvent& other);

  virtual void write(FILE* file);

};

inline bool A2EventDrain::operator==(const AEvent& other)
{
  assert(false);
}

inline bool A2EventDrain::operator!=(const AEvent& other)
{
  assert(false);
}

inline void A2EventDrain::write(FILE* file)
{
  fprintf(file, "", this);
}

