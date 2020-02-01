#pragma once

#include "AEventEncounter.h"

using namespace types;

// 1/22 19:39:52.829  ENCOUNTER_END,663,"Lucifron",9,40,1

class EventEncounterEnd : public AEventEncounter
{

public:

  EventEncounterEnd(WLogFileReader* reader) :
    AEventEncounter(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventEncounterEnd() = default;
  EventEncounterEnd(const EventEncounterEnd&) = delete;
  EventEncounterEnd &operator=(const EventEncounterEnd&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventEncounterEnd::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventEncounterEnd::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventEncounterEnd::write(FILE* file)
{
  fprintf(file, "", this);
}

