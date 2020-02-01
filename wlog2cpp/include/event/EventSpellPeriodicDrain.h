#pragma once

#include "AEventAdvancedSpell.h"
#include "A2EventDrain.h"

using namespace types;


class EventSpellPeriodicDrain : public AEventAdvancedSpell, public A2EventDrain
{

public:

  EventSpellPeriodicDrain(WLogFileReader* reader) :
    AEventAdvancedSpell(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSpellPeriodicDrain() = default;
  EventSpellPeriodicDrain(const EventSpellPeriodicDrain&) = delete;
  EventSpellPeriodicDrain &operator=(const EventSpellPeriodicDrain&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellPeriodicDrain::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSpellPeriodicDrain::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellPeriodicDrain::write(FILE* file)
{
  fprintf(file, "", this);
}

