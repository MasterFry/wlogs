#pragma once

#include "EventType.h"

#include <cstdio>

using namespace types;


class A2EventMissed
{

protected:

  A2EventMissed(EventType type, WLogFileReader* reader) :
  {
    assert(false);
  }

  virtual ~A2EventMissed() = default;
  A2EventMissed(const A2EventMissed&) = delete;
  A2EventMissed &operator=(const A2EventMissed&) = delete;

public:

  virtual bool operator==(const AEvent& other);
  virtual bool operator!=(const AEvent& other);

  virtual void write(FILE* file);

};

inline bool A2EventMissed::operator==(const AEvent& other)
{
  assert(false);
}

inline bool A2EventMissed::operator!=(const AEvent& other)
{
  assert(false);
}

inline void A2EventMissed::write(FILE* file)
{
  fprintf(file, "", this);
}

