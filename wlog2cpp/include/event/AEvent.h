#pragma once

#include "time.h"
#include "EventType.h"

#include <cstdio>

using namespace types;

// Unknown Parameters:
// A2EventHeal: p1
// A2EventDamage: p2, p3
// EventEncounterStart: p4
// EventSpellAbsorbed: p5
// A2EventDrain: p6

class AEvent : public IWriteable
{

protected:

  time_t time;
  EventType eventType;

  AEvent(time_t time, EventType eventType) :
    time(time),
    eventType(eventType)
  {
  }

  virtual ~AEvent() = default;
  AEvent(const AEvent&) = delete;
  AEvent &operator=(const AEvent&) = delete;

public:

  virtual bool operator==(const AEvent& other);
  virtual bool operator!=(const AEvent& other);

  virtual void write(FILE* file) override;

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
  this->time.write(file);
  fputs(getCName(this->eventType), file);
}

