#pragma once

#include "AEventAdvancedSpell.h"
#include "A2EventEnergize.h"

using namespace types;

class EventSpellPeriodicEnergize : public AEventAdvancedSpell, public A2EventEnergize
{

public:

  EventSpellPeriodicEnergize(time_t time, WLogFileReader* reader) :
    AEventAdvancedSpell(time, EventType::SPELL_PERIODIC_ENERGIZE, reader),
    A2EventEnergize(EventType::SPELL_PERIODIC_ENERGIZE, reader)
  {
  }

  virtual ~EventSpellPeriodicEnergize() = default;
  EventSpellPeriodicEnergize(const EventSpellPeriodicEnergize&) = delete;
  EventSpellPeriodicEnergize &operator=(const EventSpellPeriodicEnergize&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellPeriodicEnergize::operator==(const AEvent& other)
{
  return AEventAdvancedSpell::operator==(other) && A2EventEnergize::operator==(other);
}

inline bool EventSpellPeriodicEnergize::operator!=(const AEvent& other)
{
  return AEventAdvancedSpell::operator!=(other) || A2EventEnergize::operator!=(other);
}

inline void EventSpellPeriodicEnergize::write(FILE* file)
{
  AEventAdvancedSpell::write(file);
  A2EventEnergize::write(file);
}
