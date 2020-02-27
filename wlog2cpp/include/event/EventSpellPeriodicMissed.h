#pragma once

#include "AEventBaseSpell.h"
#include "A2EventMissed.h"

using namespace types;

class EventSpellPeriodicMissed : public AEventBaseSpell, public A2EventMissed
{

public:

  EventSpellPeriodicMissed(time_t time, WLogFileReader* reader) :
    AEventBaseSpell(time, EventType::SPELL_PERIODIC_MISSED, reader),
    A2EventMissed(EventType::SPELL_PERIODIC_MISSED, reader)
  {
  }

  virtual ~EventSpellPeriodicMissed() = default;
  EventSpellPeriodicMissed(const EventSpellPeriodicMissed&) = delete;
  EventSpellPeriodicMissed &operator=(const EventSpellPeriodicMissed&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellPeriodicMissed::operator==(const AEvent& other)
{
  return AEventBaseSpell::operator==(other) && A2EventMissed::operator==(other);
}

inline bool EventSpellPeriodicMissed::operator!=(const AEvent& other)
{
  return AEventBaseSpell::operator!=(other) || A2EventMissed::operator!=(other);
}

inline void EventSpellPeriodicMissed::write(FILE* file)
{
  AEventBaseSpell::write(file);
  A2EventMissed::write(file);
}
