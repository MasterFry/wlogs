#pragma once

#include "EventType.h"

#include <cstdio>

using namespace types;


class A2EventExtraSpell
{

protected:

  A2EventExtraSpell(EventType type, WLogFileReader* reader) :
  {
    assert(false);
  }

  virtual ~A2EventExtraSpell() = default;
  A2EventExtraSpell(const A2EventExtraSpell&) = delete;
  A2EventExtraSpell &operator=(const A2EventExtraSpell&) = delete;

public:

  virtual bool operator==(const AEvent& other);
  virtual bool operator!=(const AEvent& other);

  virtual void write(FILE* file);

};

inline bool A2EventExtraSpell::operator==(const AEvent& other)
{
  assert(false);
}

inline bool A2EventExtraSpell::operator!=(const AEvent& other)
{
  assert(false);
}

inline void A2EventExtraSpell::write(FILE* file)
{
  fprintf(file, "", this);
}

