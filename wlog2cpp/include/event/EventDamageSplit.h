#pragma once

#include "AEventAdvancedSpell.h"
#include "A2EventDamage.h"

using namespace types;


class EventDamageSplit : public AEventAdvancedSpell, public A2EventDamage
{

public:

  EventDamageSplit(WLogFileReader* reader) :
    AEventAdvancedSpell(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventDamageSplit() = default;
  EventDamageSplit(const EventDamageSplit&) = delete;
  EventDamageSplit &operator=(const EventDamageSplit&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventDamageSplit::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventDamageSplit::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventDamageSplit::write(FILE* file)
{
  fprintf(file, "", this);
}

