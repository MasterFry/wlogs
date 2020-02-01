#pragma once

#include "AEventBaseSpell.h"
#include "A2EventMissed.h"

using namespace types;


class EventSpellMissed : public AEventBaseSpell, public A2EventMissed
{

public:

  EventSpellMissed(WLogFileReader* reader) :
    AEventBaseSpell(EventType, reader)
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
  assert(false);
}

inline bool EventSpellMissed::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellMissed::write(FILE* file)
{
  fprintf(file, "", this);
}

