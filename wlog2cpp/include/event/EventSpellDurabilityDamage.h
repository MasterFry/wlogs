#pragma once

#include "AEventBaseSpell.h"

using namespace types;


class EventSpellDurabilityDamage : public AEventBaseSpell
{

public:

  EventSpellDurabilityDamage(WLogFileReader* reader) :
    AEventBaseSpell(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSpellDurabilityDamage() = default;
  EventSpellDurabilityDamage(const EventSpellDurabilityDamage&) = delete;
  EventSpellDurabilityDamage &operator=(const EventSpellDurabilityDamage&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellDurabilityDamage::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSpellDurabilityDamage::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellDurabilityDamage::write(FILE* file)
{
  fprintf(file, "", this);
}

