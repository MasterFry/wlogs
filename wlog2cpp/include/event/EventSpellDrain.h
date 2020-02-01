#pragma once

#include "AEventAdvancedSpell.h"
#include "A2EventDrain.h"

using namespace types;


class EventSpellDrain : public AEventAdvancedSpell, public A2EventDrain
{

public:

  EventSpellDrain(WLogFileReader* reader) :
    AEventAdvancedSpell(EventType, reader)
  {
    assert(false);
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
  assert(false);
}

inline bool EventSpellDrain::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellDrain::write(FILE* file)
{
  fprintf(file, "", this);
}

