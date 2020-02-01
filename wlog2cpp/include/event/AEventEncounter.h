#pragma once

#include "AEvent.h"

using namespace types;

// 1/22 19:39:52.829  ENCOUNTER_START,663,"Lucifron",9,40,409
// 1/22 19:39:52.829  ENCOUNTER_END,663,"Lucifron",9,40,1

class AEventEncounter : public AEvent
{

protected:

  AEventEncounter(EventType type, WLogFileReader* reader) :
    AEvent(type, reader)
  {
    assert(false);
  }

  virtual ~AEventEncounter() = default;
  AEventEncounter(const AEventEncounter&) = delete;
  AEventEncounter &operator=(const AEventEncounter&) = delete;

public:

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool AEventEncounter::operator==(const AEvent& other)
{
  assert(false);
}

inline bool AEventEncounter::operator!=(const AEvent& other)
{
  assert(false);
}

inline void AEventEncounter::write(FILE* file)
{
  fprintf(file, "", this);
}

