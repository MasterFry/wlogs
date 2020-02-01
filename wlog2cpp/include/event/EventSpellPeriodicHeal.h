#pragma once

#include "AEventAdvancedSpell.h"
#include "A2EventHeal.h"

using namespace types;


class EventSpellPeriodicHeal : public AEventAdvancedSpell, public A2EventHeal
{

public:

  EventSpellPeriodicHeal(WLogFileReader* reader) :
    AEventAdvancedSpell(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSpellPeriodicHeal() = default;
  EventSpellPeriodicHeal(const EventSpellPeriodicHeal&) = delete;
  EventSpellPeriodicHeal &operator=(const EventSpellPeriodicHeal&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellPeriodicHeal::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSpellPeriodicHeal::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellPeriodicHeal::write(FILE* file)
{
  fprintf(file, "", this);
}

