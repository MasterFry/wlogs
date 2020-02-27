#pragma once

#include "AEventAdvancedSpell.h"
#include "A2EventDrain.h"

using namespace types;

class EventSpellDrain : public AEventAdvancedSpell, public A2EventDrain
{

public:

  EventSpellDrain(time_t time, WLogFileReader* reader) :
    AEventAdvancedSpell(time, EventType::SPELL_DRAIN, reader),
    A2EventDrain(EventType::SPELL_DRAIN, reader)
  {
  }

  virtual ~EventSpellDrain() = default;
  EventSpellDrain(const EventSpellDrain&) = delete;
  EventSpellDrain &operator=(const EventSpellDrain&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellDrain::operator==(const AEvent& other)
{
  return AEventAdvancedSpell::operator==(other) && A2EventDrain::operator==(other);
}

inline bool EventSpellDrain::operator!=(const AEvent& other)
{
  return AEventAdvancedSpell::operator!=(other) || A2EventDrain::operator!=(other);
}

inline void EventSpellDrain::write(FILE* file)
{
  AEventAdvancedSpell::write(file);
  A2EventDrain::write(file);
}
