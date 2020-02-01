#pragma once

#include "AEventAdvancedSpell.h"
#include "A2EventDamage.h"

using namespace types;


class EventSpellPeriodicDamage : public AEventAdvancedSpell, public A2EventDamage
{

public:

  EventSpellPeriodicDamage(WLogFileReader* reader) :
    AEventAdvancedSpell(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSpellPeriodicDamage() = default;
  EventSpellPeriodicDamage(const EventSpellPeriodicDamage&) = delete;
  EventSpellPeriodicDamage &operator=(const EventSpellPeriodicDamage&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellPeriodicDamage::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSpellPeriodicDamage::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellPeriodicDamage::write(FILE* file)
{
  fprintf(file, "", this);
}

