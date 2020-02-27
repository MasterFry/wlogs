#pragma once

#include "AEventAdvancedSpell.h"
#include "A2EventHeal.h"

using namespace types;

class EventSpellHeal : public AEventAdvancedSpell, public A2EventHeal
{

public:

  EventSpellHeal(time_t time, WLogFileReader* reader) :
    AEventAdvancedSpell(time, EventType::SPELL_HEAL, reader),
    A2EventHeal(EventType::SPELL_HEAL, reader)
  {
    assert(false);
  }

  virtual ~EventSpellHeal() = default;
  EventSpellHeal(const EventSpellHeal&) = delete;
  EventSpellHeal &operator=(const EventSpellHeal&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellHeal::operator==(const AEvent& other)
{
  return AEventAdvancedSpell::operator==(other) && A2EventHeal::operator==(other);
}

inline bool EventSpellHeal::operator!=(const AEvent& other)
{
  return AEventAdvancedSpell::operator!=(other) || A2EventHeal::operator!=(other);
}

inline void EventSpellHeal::write(FILE* file)
{
  AEventAdvancedSpell::write(file);
  A2EventHeal::write(file);
}
