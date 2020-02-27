#pragma once

#include "AEvent.h"

using namespace types;

// 1/22 19:26:49.388  COMBAT_LOG_VERSION,9,ADVANCED_LOG_ENABLED,1,BUILD_VERSION,1.13.3,PROJECT_ID,2

class EventCombatLogVersion : public AEvent
{

public:

  EventCombatLogVersion(time_t time, WLogFileReader* reader) :
    AEvent(time, EventType, reader)
  {
    assert(false);
  }

  virtual ~EventCombatLogVersion() = default;
  EventCombatLogVersion(const EventCombatLogVersion&) = delete;
  EventCombatLogVersion &operator=(const EventCombatLogVersion&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventCombatLogVersion::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventCombatLogVersion::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventCombatLogVersion::write(FILE* file)
{
  fprintf(file, "", this);
}

