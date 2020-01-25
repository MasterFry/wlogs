#pragma once

#include "Event.h"

class EventAdvanced : public Event
{

public:

  EventAdvanced(EVENT_TYPE type, time_t time, GUID& srcGUID, unitflag_t srcFlags, GUID& destGUID, unitflag_t destFlags, GUID& unitGUID, GUID& ownerGUID, std::string line) :
    Event(type, time, srcGUID, srcFlags, destGUID, destFlags, line),
    unitGUID(unitGUID),
    ownerGUID(ownerGUID)
  {
  }

  // bool operator==(const Event& other) const override;

  // bool operator!=(const Event& other) const override
  // {
  //   return !((*this) == other);
  // }
  
  bool operator==(const EventAdvanced& other) const
  {
    if(unitGUID != other.unitGUID || ownerGUID != other.ownerGUID)
      return false;
    return Event::operator==(other);
  }

  bool operator!=(const EventAdvanced& other) const
  {
    return !((*this) == other);
  }
  
  bool hasAdvancedParams() const override
  {
    return true;
  }

private:

  GUID unitGUID;
  GUID ownerGUID;

};