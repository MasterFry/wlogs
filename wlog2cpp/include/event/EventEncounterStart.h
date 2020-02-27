#pragma once

#include "AEventEncounter.h"

using namespace types;

// 1/22 19:39:52.829  ENCOUNTER_START,663,"Lucifron",9,40,409

class EventEncounterStart : public AEventEncounter
{

protected:

  uint32_t p4;

public:

  EventEncounterStart(time_t time, WLogFileReader* reader) :
    AEventEncounter(time, EventType::ENCOUNTER_START, reader),
    p4(reader->readUnsigned())
  {
  }

  virtual ~EventEncounterStart() = default;
  EventEncounterStart(const EventEncounterStart&) = delete;
  EventEncounterStart &operator=(const EventEncounterStart&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventEncounterStart::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventEncounterStart::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventEncounterStart::write(FILE* file)
{
  AEventEncounter::write(file);
  fprintf(file, ",%d", this->p4);
}

