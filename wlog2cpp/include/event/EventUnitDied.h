#pragma once

#include "AEventBase.h"

using namespace types;


class EventUnitDied : public AEventBase
{

public:

  EventUnitDied(WLogFileReader* reader) :
    AEventBase(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventUnitDied() = default;
  EventUnitDied(const EventUnitDied&) = delete;
  EventUnitDied &operator=(const EventUnitDied&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventUnitDied::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventUnitDied::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventUnitDied::write(FILE* file)
{
  fprintf(file, "", this);
}

