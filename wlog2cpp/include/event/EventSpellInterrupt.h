#pragma once

#include "AEventBaseSpell.h"
#include "A2EventExtraSpell.h"

using namespace types;

class EventSpellInterrupt : public AEventBaseSpell, public A2EventExtraSpell
{

public:

  EventSpellInterrupt(time_t time, WLogFileReader* reader) :
    AEventBaseSpell(time, EventType::SPELL_INTERRUPT, reader),
    A2EventExtraSpell(EventType::SPELL_INTERRUPT, reader)
  {
  }

  virtual ~EventSpellInterrupt() = default;
  EventSpellInterrupt(const EventSpellInterrupt&) = delete;
  EventSpellInterrupt &operator=(const EventSpellInterrupt&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellInterrupt::operator==(const AEvent& other)
{
  return AEventBaseSpell::operator==(other) && A2EventExtraSpell::operator==(other);
}

inline bool EventSpellInterrupt::operator!=(const AEvent& other)
{
  return AEventBaseSpell::operator!=(other) || A2EventExtraSpell::operator!=(other);
}

inline void EventSpellInterrupt::write(FILE* file)
{
  AEventBaseSpell::write(file);
  A2EventExtraSpell::write(file);
}
