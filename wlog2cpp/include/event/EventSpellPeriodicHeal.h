#pragma once

#include "AEventAdvancedSpell.h"
#include "A2EventHeal.h"

using namespace types;

class EventSpellPeriodicHeal : public AEventAdvancedSpell, public A2EventHeal
{

public:

  EventSpellPeriodicHeal(time_t time, WLogFileReader* reader) :
    AEventAdvancedSpell(time, EventType::SPELL_PERIODIC_HEAL, reader),
    A2EventHeal(EventType::SPELL_PERIODIC_HEAL, reader)
  {
  }

  virtual ~EventSpellPeriodicHeal() = default;
  EventSpellPeriodicHeal(const EventSpellPeriodicHeal&) = delete;
  EventSpellPeriodicHeal &operator=(const EventSpellPeriodicHeal&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellPeriodicHeal::operator==(const AEvent& other)
{
  return AEventAdvancedSpell::operator==(other) && A2EventHeal::operator==(other);
}

inline bool EventSpellPeriodicHeal::operator!=(const AEvent& other)
{
  return AEventAdvancedSpell::operator!=(other) || A2EventHeal::operator!=(other);
}

inline void EventSpellPeriodicHeal::write(FILE* file)
{
  AEventAdvancedSpell::write(file);
  A2EventHeal::write(file);
}
