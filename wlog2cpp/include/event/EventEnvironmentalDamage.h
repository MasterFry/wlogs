#pragma once

#include "AEventAdvanced.h"
#include "A2EventDamage.h"

using namespace types;


class EventEnvironmentalDamage : public AEventAdvanced, public A2EventDamage
{

public:

  EventEnvironmentalDamage(WLogFileReader* reader) :
    AEventAdvanced(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventEnvironmentalDamage() = default;
  EventEnvironmentalDamage(const EventEnvironmentalDamage&) = delete;
  EventEnvironmentalDamage &operator=(const EventEnvironmentalDamage&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventEnvironmentalDamage::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventEnvironmentalDamage::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventEnvironmentalDamage::write(FILE* file)
{
  fprintf(file, "", this);
}

