#pragma once

#include "EventType.h"

#include <cstdio>

using namespace types;

//  1:  spellName
//  2:  itemId
//  3:  itemName

class A2EventEnchant
{

protected:

  A2EventEnchant(EventType type, WLogFileReader* reader) :
  {
    assert(false);
  }

  virtual ~A2EventEnchant() = default;
  A2EventEnchant(const A2EventEnchant&) = delete;
  A2EventEnchant &operator=(const A2EventEnchant&) = delete;

public:

  virtual bool operator==(const AEvent& other);
  virtual bool operator!=(const AEvent& other);

  virtual void write(FILE* file);

};

inline bool A2EventEnchant::operator==(const AEvent& other)
{
  assert(false);
}

inline bool A2EventEnchant::operator!=(const AEvent& other)
{
  assert(false);
}

inline void A2EventEnchant::write(FILE* file)
{
  fprintf(file, "", this);
}

