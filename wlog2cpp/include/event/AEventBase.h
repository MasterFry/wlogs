#pragma once

#include "std.h"
#include "AEvent.h"
#include "AGUID.h"
#include "WLogFileReader.h"

using namespace types;

// 1 : Source GUID
//       Player-4701-00B442E4
// 2 : Source Name
//       "Doncarleon-Mograine"
// 3 : Source Unit Flags
//       0x514
// 4 : Source Raid Flags
//       0x0
// 5 : Destination GUID
//       Creature-0-4469-409-26884-11671-000428A101
// 6 : Destination Name
//       "Core Hound"
// 7 : Destination Unit Flags
//       0xa48
// 8 : Destination Raid Flags
//       0x0

class AEventBase : public AEvent
{

protected:

  AGUID* srcGUID;
  string_t srcName;
  uint32_t srcFlags;
  uint32_t srcRaidFlags;
  AGUID* destGUID;
  string_t destName;
  uint32_t destFlags;
  uint32_t destRaidFlags;

  AEventBase(time_t time, EventType eventType, WLogFileReader* reader) :
    AEvent(time, eventType),
    srcGUID(reader->readGUID()),
    srcName(reader->readString()),
    srcFlags(reader->readUnsigned(',', 16)),
    srcRaidFlags(reader->readUnsigned(',', 16)),
    destGUID(reader->readGUID()),
    destName(reader->readString()),
    destFlags(reader->readUnsigned(',', 16)),
    destRaidFlags(reader->readUnsigned(',', 16))
  {
  }

  virtual ~AEventBase() = default;
  AEventBase(const AEventBase&) = delete;
  AEventBase &operator=(const AEventBase&) = delete;

public:

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool AEventBase::operator==(const AEvent& other)
{
  assert(false);
}

inline bool AEventBase::operator!=(const AEvent& other)
{
  assert(false);
}

inline void AEventBase::write(FILE* file)
{
  AEvent::write(file);
  this->srcGUID->write(file);
  fprintf(file, ",\"%s\",%#x,%#x",
    this->srcName,
    this->srcFlags,
    this->srcRaidFlags
  );
  this->destGUID->write(file);
  fprintf(file, ",\"%s\",%#x,%#x",
    this->destName,
    this->destFlags,
    this->destRaidFlags
  );
}

