#pragma once

#include "AEventAdvanced.h"
#include "A2EventDamage.h"

using namespace types;


class EventSwingDamage : public AEventAdvanced, public A2EventDamage
{

public:

  EventSwingDamage(WLogFileReader* reader) :
    AEventAdvanced(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSwingDamage() = default;
  EventSwingDamage(const EventSwingDamage&) = delete;
  EventSwingDamage &operator=(const EventSwingDamage&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSwingDamage::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSwingDamage::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSwingDamage::write(FILE* file)
{
  fprintf(file, "", this);
}

