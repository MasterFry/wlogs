#pragma once

#include "AEventAdvancedSpell.h"
#include "A2EventDamage.h"

using namespace types;


class EventRangeDamage : public AEventAdvancedSpell, public A2EventDamage
{

public:

  EventRangeDamage(WLogFileReader* reader) :
    AEventAdvancedSpell(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventRangeDamage() = default;
  EventRangeDamage(const EventRangeDamage&) = delete;
  EventRangeDamage &operator=(const EventRangeDamage&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventRangeDamage::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventRangeDamage::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventRangeDamage::write(FILE* file)
{
  fprintf(file, "", this);
}

