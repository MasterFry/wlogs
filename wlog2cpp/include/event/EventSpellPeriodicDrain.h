#pragma once

#include "AEventAdvancedSpell.h"
#include "A2EventDrain.h"

using namespace types;

class EventSpellPeriodicDrain : public AEventAdvancedSpell, public A2EventDrain
{

public:

  EventSpellPeriodicDrain(time_t time, WLogFileReader* reader) :
    AEventAdvancedSpell(time, EventType::SPELL_PERIODIC_DRAIN, reader),
    A2EventDrain(EventType::SPELL_PERIODIC_DRAIN, reader)
  {
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
  return AEventAdvancedSpell::operator==(other) && A2EventDrain::operator==(other);
}

inline bool EventSpellPeriodicDrain::operator!=(const AEvent& other)
{
  return AEventAdvancedSpell::operator!=(other) || A2EventDrain::operator!=(other);
}

inline void EventSpellPeriodicDrain::write(FILE* file)
{
  AEventAdvancedSpell::write(file);
  A2EventDrain::write(file);
}
