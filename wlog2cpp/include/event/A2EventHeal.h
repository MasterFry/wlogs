#pragma once

#include "EventType.h"

#include <cstdio>

using namespace types;

// 296,296,0,0,nil
// 1224,1224,1224,0,nil
//  1:  amount
//  2:  overhealing
//  3:  absorbed
//  4:  ?
//  5:  critical: nil / 1

class A2EventHeal
{

protected:

  A2EventHeal(EventType type, WLogFileReader* reader) :
  {
    assert(false);
  }

  virtual ~A2EventHeal() = default;
  A2EventHeal(const A2EventHeal&) = delete;
  A2EventHeal &operator=(const A2EventHeal&) = delete;

public:

  virtual bool operator==(const AEvent& other);
  virtual bool operator!=(const AEvent& other);

  virtual void write(FILE* file);

};

inline bool A2EventHeal::operator==(const AEvent& other)
{
  assert(false);
}

inline bool A2EventHeal::operator!=(const AEvent& other)
{
  assert(false);
}

inline void A2EventHeal::write(FILE* file)
{
  fprintf(file, "", this);
}

