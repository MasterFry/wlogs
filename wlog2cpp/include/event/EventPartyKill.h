#pragma once

#include "AEventBase.h"

using namespace types;


class EventPartyKill : public AEventBase
{

public:

  EventPartyKill(time_t time, WLogFileReader* reader) :
    AEventBase(time, EventType, reader)
  {
    assert(false);
  }

  virtual ~EventPartyKill() = default;
  EventPartyKill(const EventPartyKill&) = delete;
  EventPartyKill &operator=(const EventPartyKill&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventPartyKill::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventPartyKill::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventPartyKill::write(FILE* file)
{
  fprintf(file, "", this);
}

