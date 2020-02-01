#pragma once

#include "AEventBaseSpell.h"
#include "A2EventMissed.h"

using namespace types;


class EventSpellPeriodicMissed : public AEventBaseSpell, public A2EventMissed
{

public:

  EventSpellPeriodicMissed(WLogFileReader* reader) :
    AEventBaseSpell(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSpellPeriodicMissed() = default;
  EventSpellPeriodicMissed(const EventSpellPeriodicMissed&) = delete;
  EventSpellPeriodicMissed &operator=(const EventSpellPeriodicMissed&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellPeriodicMissed::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSpellPeriodicMissed::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellPeriodicMissed::write(FILE* file)
{
  fprintf(file, "", this);
}

