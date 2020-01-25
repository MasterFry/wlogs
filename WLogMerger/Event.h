#pragma once

#include "event-definitions.h"
#include "UnitFlag.h"
#include "GUID.h"
#include "Time.h"

class Event
{

public:

  Event(EVENT_TYPE type, time_t time, GUID& srcGUID, unitflag_t srcFlags, GUID& destGUID, unitflag_t destFlags, std::string line) :
    type(type),
    time(time),
    srcGUID(std::move(srcGUID)),
    srcFlags(srcFlags),
    destGUID(std::move(destGUID)),
    destFlags(destFlags),
    line(line)
  {
  }

  bool operator==(const Event& other) const
  {
    return type == other.type &&
           Time::compare(time, other.time) == 0 &&
           srcGUID == other.srcGUID &&
           srcFlags == other.srcFlags &&
           destGUID == other.destGUID &&
           destFlags == other.destFlags &&
           line.length() == other.line.length();
  }

  bool operator!=(const Event& other) const
  {
    return !((*this) == other);
  }

  std::string getLine() const
  {
    return line;
  }

  virtual bool hasAdvancedParams() const
  {
    return false;
  }

private:

  EVENT_TYPE type;
  time_t time;
  GUID srcGUID;
  unitflag_t srcFlags;
  GUID destGUID;
  unitflag_t destFlags;
  std::string line;

};
