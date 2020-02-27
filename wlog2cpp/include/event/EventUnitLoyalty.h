#pragma once

#include "AEventBase.h"

using namespace types;

class EventUnitLoyalty : public AEventBase
{

public:

  EventUnitLoyalty(time_t time, WLogFileReader* reader) :
    AEventBase(time, EventType::UNIT_LOYALTY, reader)
  {
  }

  virtual ~EventUnitLoyalty() = default;
  EventUnitLoyalty(const EventUnitLoyalty&) = delete;
  EventUnitLoyalty &operator=(const EventUnitLoyalty&) = delete;

};