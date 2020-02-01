#pragma once

#include "AEventBase.h"

using namespace types;


class EventUnitLoyalty : public AEventBase
{

public:

  EventUnitLoyalty(WLogFileReader* reader) :
    AEventBase(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventUnitLoyalty() = default;
  EventUnitLoyalty(const EventUnitLoyalty&) = delete;
  EventUnitLoyalty &operator=(const EventUnitLoyalty&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventUnitLoyalty::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventUnitLoyalty::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventUnitLoyalty::write(FILE* file)
{
  fprintf(file, "", this);
}

