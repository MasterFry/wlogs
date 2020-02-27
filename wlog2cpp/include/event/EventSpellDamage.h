#pragma once

#include "AEventAdvancedSpell.h"
#include "A2EventDamage.h"

using namespace types;

class EventSpellDamage : public AEventAdvancedSpell, public A2EventDamage
{

public:

  EventSpellDamage(time_t time, WLogFileReader* reader) :
    AEventAdvancedSpell(time, EventType::SPELL_DAMAGE, reader),
    A2EventDamage(EventType::SPELL_DAMAGE, reader)
  {
  }

  virtual ~EventSpellDamage() = default;
  EventSpellDamage(const EventSpellDamage&) = delete;
  EventSpellDamage &operator=(const EventSpellDamage&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellDamage::operator==(const AEvent& other)
{
  return AEventAdvancedSpell::operator==(other) && A2EventDamage::operator==(other);
}

inline bool EventSpellDamage::operator!=(const AEvent& other)
{
  return AEventAdvancedSpell::operator!=(other) || A2EventDamage::operator!=(other);
}

inline void EventSpellDamage::write(FILE* file)
{
  AEventAdvancedSpell::write(file);
  A2EventDamage::write(file);
}
