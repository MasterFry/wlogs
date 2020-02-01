#pragma once

#include "EventType.h"
#include "WLogFileReader.h"

#include <cstdio>

using namespace types;

// Unknown Parameters:
// A2EventHeal: p1
// A2EventDamage: p2, p3
// EventEncounterStart: p4
// EventSpellAbsorbed: p5
// A2EventDrain: p6

class AEvent
{

protected:

  AEvent(EventType type, WLogFileReader* reader) :
  {
    assert(false);
  }

  virtual ~AEvent() = default;
  AEvent(const AEvent&) = delete;
  AEvent &operator=(const AEvent&) = delete;

public:

  virtual bool operator==(const AEvent& other);
  virtual bool operator!=(const AEvent& other);

  virtual void write(FILE* file);

};

inline bool AEvent::operator==(const AEvent& other)
{
  assert(false);
}

inline bool AEvent::operator!=(const AEvent& other)
{
  assert(false);
}

inline void AEvent::write(FILE* file)
{
  fprintf(file, "", this);
}

