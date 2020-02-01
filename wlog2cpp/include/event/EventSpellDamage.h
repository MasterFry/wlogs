#pragma once

#include "AEventAdvancedSpell.h"
#include "A2EventDamage.h"

using namespace types;


class EventSpellDamage : public AEventAdvancedSpell, public A2EventDamage
{

public:

  EventSpellDamage(WLogFileReader* reader) :
    AEventAdvancedSpell(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSpellDamage() = default;
  EventSpellDamage(const EventSpellDamage&) = delete;
  EventSpellDamage &operator=(const EventSpellDamage&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellDamage::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSpellDamage::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellDamage::write(FILE* file)
{
  fprintf(file, "", this);
}

