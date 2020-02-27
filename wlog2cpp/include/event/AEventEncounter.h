#pragma once

#include "std.h"
#include "AEvent.h"

using namespace types;

// 1/22 19:39:52.829  ENCOUNTER_START,663,"Lucifron",9,40,409
// 1/22 19:39:52.829  ENCOUNTER_END,663,"Lucifron",9,40,1

class AEventEncounter : public AEvent
{

protected:

  uint32_t encounterId;
  string_t encounterName;
  uint8_t difficultyId;
  uint8_t playerCount;

  AEventEncounter(time_t time, EventType eventType, WLogFileReader* reader) :
    AEvent(time, eventType),
    encounterId(reader->readUnsigned()),
    encounterName(reader->readString()),
    difficultyId(reader->readUnsigned()),
    playerCount(reader->readUnsigned())
  {
    assert(
      eventType == EventType::ENCOUNTER_START ||
      eventType == EventType::ENCOUNTER_END
    );
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
  AEvent::write(file);
  fprintf(file, ",%d,\"%s\",%d,%d",
    this->encounterId,
    this->encounterName,
    this->difficultyId,
    this->playerCount
  );
}
