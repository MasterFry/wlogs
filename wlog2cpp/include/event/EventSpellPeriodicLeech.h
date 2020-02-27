#pragma once

#include "AEventAdvancedSpell.h"
#include "A2EventDrain.h"

using namespace types;

class EventSpellPeriodicLeech : public AEventAdvancedSpell, public A2EventDrain
{

public:

  EventSpellPeriodicLeech(time_t time, WLogFileReader* reader) :
    AEventAdvancedSpell(time, EventType::SPELL_PERIODIC_LEECH, reader),
    A2EventDrain(EventType::SPELL_PERIODIC_LEECH, reader)
  {
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
  return AEventAdvancedSpell::operator==(other) && A2EventDrain::operator==(other);
}

inline bool EventSpellPeriodicLeech::operator!=(const AEvent& other)
{
  return AEventAdvancedSpell::operator!=(other) || A2EventDrain::operator!=(other);
}

inline void EventSpellPeriodicLeech::write(FILE* file)
{
  AEventAdvancedSpell::write(file);
  A2EventDrain::write(file);
}
