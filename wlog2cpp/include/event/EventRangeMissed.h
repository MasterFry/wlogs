#pragma once

#include "AEventBaseSpell.h"
#include "A2EventMissed.h"

using namespace types;


class EventRangeMissed : public AEventBaseSpell, public A2EventMissed
{

public:

  EventRangeMissed(WLogFileReader* reader) :
    AEventBaseSpell(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventRangeMissed() = default;
  EventRangeMissed(const EventRangeMissed&) = delete;
  EventRangeMissed &operator=(const EventRangeMissed&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventRangeMissed::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventRangeMissed::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventRangeMissed::write(FILE* file)
{
  fprintf(file, "", this);
}

