#pragma once

#include "AEventBaseSpell.h"
#include "A2EventExtraSpell.h"

using namespace types;


class EventSpellInterrupt : public AEventBaseSpell, public A2EventExtraSpell
{

public:

  EventSpellInterrupt(WLogFileReader* reader) :
    AEventBaseSpell(EventType, reader)
  {
    assert(false);
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
  assert(false);
}

inline bool EventSpellInterrupt::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellInterrupt::write(FILE* file)
{
  fprintf(file, "", this);
}

