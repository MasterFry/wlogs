#pragma once

#include "AEventBaseSpell.h"
#include "A2EventMissed.h"

using namespace types;


class EventDamageShieldMissed : public AEventBaseSpell, public A2EventMissed
{

public:

  EventDamageShieldMissed(WLogFileReader* reader) :
    AEventBaseSpell(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventDamageShieldMissed() = default;
  EventDamageShieldMissed(const EventDamageShieldMissed&) = delete;
  EventDamageShieldMissed &operator=(const EventDamageShieldMissed&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventDamageShieldMissed::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventDamageShieldMissed::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventDamageShieldMissed::write(FILE* file)
{
  fprintf(file, "", this);
}

