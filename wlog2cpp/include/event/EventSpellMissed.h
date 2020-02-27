#pragma once

#include "AEventBaseSpell.h"
#include "A2EventMissed.h"

using namespace types;


class EventSpellMissed : public AEventBaseSpell, public A2EventMissed
{

public:

  EventSpellMissed(time_t time, WLogFileReader* reader) :
    AEventBaseSpell(time, EventType::SPELL_MISSED, reader),
    A2EventMissed(EventType::SPELL_MISSED, reader)
  {
    assert(false);
  }

  virtual ~EventSpellMissed() = default;
  EventSpellMissed(const EventSpellMissed&) = delete;
  EventSpellMissed &operator=(const EventSpellMissed&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellMissed::operator==(const AEvent& other)
{
  return AEventBaseSpell::operator==(other) && A2EventMissed::operator==(other);
}

inline bool EventSpellMissed::operator!=(const AEvent& other)
{
  return AEventBaseSpell::operator!=(other) || A2EventMissed::operator!=(other);
}

inline void EventSpellMissed::write(FILE* file)
{
  AEventBaseSpell::write(file);
  A2EventMissed::write(file);
}

