#pragma once

#include "AEventBase.h"

using namespace types;

class EventUnitDied : public AEventBase
{

public:

  EventUnitDied(time_t time, WLogFileReader* reader) :
    AEventBase(time, EventType::UNIT_DIED, reader)
  {
  }

  virtual ~EventUnitDied() = default;
  EventUnitDied(const EventUnitDied&) = delete;
  EventUnitDied &operator=(const EventUnitDied&) = delete;

};
