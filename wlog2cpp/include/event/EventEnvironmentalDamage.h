#pragma once

#include "A1EventAdvanced.h"
#include "A2EventDamage.h"

using namespace types;


class EventEnvironmentalDamage : public A1EventAdvanced, public A2EventDamage
{

public:

  EventEnvironmentalDamage(time_t time, WLogFileReader* reader) :
    A1EventAdvanced(time, EventType, reader)
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

