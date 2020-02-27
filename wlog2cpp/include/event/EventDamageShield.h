#pragma once

#include "AEventAdvancedSpell.h"
#include "A2EventDamage.h"

using namespace types;


class EventDamageShield : public AEventAdvancedSpell, public A2EventDamage
{

public:

  EventDamageShield(time_t time, WLogFileReader* reader) :
    AEventAdvancedSpell(time, EventType, reader)
  {
    assert(false);
  }

  virtual ~EventDamageShield() = default;
  EventDamageShield(const EventDamageShield&) = delete;
  EventDamageShield &operator=(const EventDamageShield&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventDamageShield::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventDamageShield::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventDamageShield::write(FILE* file)
{
  fprintf(file, "", this);
}

