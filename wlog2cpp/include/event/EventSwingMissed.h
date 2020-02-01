#pragma once

#include "AEventBase.h"
#include "A2EventMissed.h"

using namespace types;


class EventSwingMissed : public AEventBase, public A2EventMissed
{

public:

  EventSwingMissed(WLogFileReader* reader) :
    AEventBase(EventType, reader)
  {
    assert(false);
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
  assert(false);
}

inline bool EventSwingMissed::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSwingMissed::write(FILE* file)
{
  fprintf(file, "", this);
}

