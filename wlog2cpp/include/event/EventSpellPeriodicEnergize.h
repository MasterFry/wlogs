#pragma once

#include "AEventAdvancedSpell.h"

using namespace types;


class EventSpellPeriodicEnergize : public AEventAdvancedSpell
{

public:

  EventSpellPeriodicEnergize(WLogFileReader* reader) :
    AEventAdvancedSpell(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSpellPeriodicEnergize() = default;
  EventSpellPeriodicEnergize(const EventSpellPeriodicEnergize&) = delete;
  EventSpellPeriodicEnergize &operator=(const EventSpellPeriodicEnergize&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellPeriodicEnergize::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSpellPeriodicEnergize::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellPeriodicEnergize::write(FILE* file)
{
  fprintf(file, "", this);
}

