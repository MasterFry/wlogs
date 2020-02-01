#pragma once

#include "AEventAdvancedSpell.h"
#include "A2EventEnergize.h"

using namespace types;


class EventSpellEnergize : public AEventAdvancedSpell, public A2EventEnergize
{

public:

  EventSpellEnergize(WLogFileReader* reader) :
    AEventAdvancedSpell(EventType, reader)
  {
    assert(false);
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
  assert(false);
}

inline bool EventSpellEnergize::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellEnergize::write(FILE* file)
{
  fprintf(file, "", this);
}

