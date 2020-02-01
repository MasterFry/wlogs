#pragma once

#include "EventType.h"

#include <cstdio>

using namespace types;

// 986,896,-1,16,0,0,0,nil,nil,nil
//  1:  amount:
//  2:  ?: 0 - 5000
//  3:  ?: -1 - 2579
//  4:  school: 0 - 127
//  5:  resisted:
//  6:  blocked:
//  7:  absorbed:
//  8:  critical: nil / 1
//  9:  glancing: nil / 1
// 10:  crushing: nil / 1

class A2EventDamage
{

protected:

  A2EventDamage(EventType type, WLogFileReader* reader) :
  {
    assert(false);
  }

  virtual ~A2EventDamage() = default;
  A2EventDamage(const A2EventDamage&) = delete;
  A2EventDamage &operator=(const A2EventDamage&) = delete;

public:

  virtual bool operator==(const AEvent& other);
  virtual bool operator!=(const AEvent& other);

  virtual void write(FILE* file);

};

inline bool A2EventDamage::operator==(const AEvent& other)
{
  assert(false);
}

inline bool A2EventDamage::operator!=(const AEvent& other)
{
  assert(false);
}

inline void A2EventDamage::write(FILE* file)
{
  fprintf(file, "", this);
}

