#pragma once

#include "AEventBase.h"
#include "A2EventMissed.h"

using namespace types;

class EventSwingMissed : public AEventBase, public A2EventMissed
{

public:

  EventSwingMissed(time_t time, WLogFileReader* reader) :
    AEventBase(time, EventType::SWING_MISSED, reader),
    A2EventMissed(EventType::SWING_MISSED, reader)
  {
  }

  virtual ~EventSwingMissed() = default;
  EventSwingMissed(const EventSwingMissed&) = delete;
  EventSwingMissed &operator=(const EventSwingMissed&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSwingMissed::operator==(const AEvent& other)
{
  return AEventBase::operator==(other) && A2EventMissed::operator==(other);
}

inline bool EventSwingMissed::operator!=(const AEvent& other)
{
  return AEventBase::operator!=(other) || A2EventMissed::operator!=(other);
}

inline void EventSwingMissed::write(FILE* file)
{
  AEventBase::write(file);
  A2EventMissed::write(file);
}
