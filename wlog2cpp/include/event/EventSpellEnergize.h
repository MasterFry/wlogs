#pragma once

#include "AEventAdvancedSpell.h"
#include "A2EventEnergize.h"

using namespace types;

class EventSpellEnergize : public AEventAdvancedSpell, public A2EventEnergize
{

public:

  EventSpellEnergize(time_t time, WLogFileReader* reader) :
    AEventAdvancedSpell(time, EventType::SPELL_ENERGIZE, reader),
    A2EventEnergize(EventType::SPELL_ENERGIZE, reader)
  {
  }

  virtual ~EventSpellEnergize() = default;
  EventSpellEnergize(const EventSpellEnergize&) = delete;
  EventSpellEnergize &operator=(const EventSpellEnergize&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellEnergize::operator==(const AEvent& other)
{
  return AEventAdvancedSpell::operator==(other) && A2EventEnergize::operator==(other);
}

inline bool EventSpellEnergize::operator!=(const AEvent& other)
{
  return AEventAdvancedSpell::operator!=(other) || A2EventEnergize::operator!=(other);
}

inline void EventSpellEnergize::write(FILE* file)
{
  AEventAdvancedSpell::write(file);
  A2EventEnergize::write(file);
}
