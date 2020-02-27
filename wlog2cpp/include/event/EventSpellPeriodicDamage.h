#pragma once

#include "AEventAdvancedSpell.h"
#include "A2EventDamage.h"

using namespace types;

class EventSpellPeriodicDamage : public AEventAdvancedSpell, public A2EventDamage
{

public:

  EventSpellPeriodicDamage(time_t time, WLogFileReader* reader) :
    AEventAdvancedSpell(time, EventType::SPELL_PERIODIC_DAMAGE, reader),
    A2EventDamage(EventType::SPELL_PERIODIC_DAMAGE, reader)
  {
  }

  virtual ~EventSpellPeriodicDamage() = default;
  EventSpellPeriodicDamage(const EventSpellPeriodicDamage&) = delete;
  EventSpellPeriodicDamage &operator=(const EventSpellPeriodicDamage&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellPeriodicDamage::operator==(const AEvent& other)
{
  return AEventAdvancedSpell::operator==(other) && A2EventDamage::operator==(other);
}

inline bool EventSpellPeriodicDamage::operator!=(const AEvent& other)
{
  return AEventAdvancedSpell::operator!=(other) || A2EventDamage::operator!=(other);
}

inline void EventSpellPeriodicDamage::write(FILE* file)
{
  AEventAdvancedSpell::write(file);
  A2EventDamage::write(file);
}
