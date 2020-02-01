#pragma once

#include "AEventAdvancedSpell.h"
#include "A2EventDrain.h"

using namespace types;


class EventSpellPeriodicLeech : public AEventAdvancedSpell, public A2EventDrain
{

public:

  EventSpellPeriodicLeech(WLogFileReader* reader) :
    AEventAdvancedSpell(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSpellPeriodicLeech() = default;
  EventSpellPeriodicLeech(const EventSpellPeriodicLeech&) = delete;
  EventSpellPeriodicLeech &operator=(const EventSpellPeriodicLeech&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellPeriodicLeech::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSpellPeriodicLeech::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellPeriodicLeech::write(FILE* file)
{
  fprintf(file, "", this);
}

