#pragma once

#include "AEvent.h"

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

  AEventBase(EventType type, WLogFileReader* reader) :
    AEvent(type, reader)
  {
    assert(false);
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
  fprintf(file, "", this);
}

