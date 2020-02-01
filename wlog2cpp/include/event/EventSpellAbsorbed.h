#pragma once

#include "AEventBase.h"

using namespace types;

// BASE,                          Player-4701-0094E8DE,"Beemo-Mograine",0x514,0x0, 10193,"Mana Shield",0x40, 570,1593
// BASE, 21333,"Lava Breath",0x4, Player-4701-00B48D7F,"Qopy-Mograine",0x511,0x0,  13033,"Ice Barrier",0x10, 524,722

class EventSpellAbsorbed : public AEventBase
{

public:

  EventSpellAbsorbed(WLogFileReader* reader) :
    AEventBase(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSpellAbsorbed() = default;
  EventSpellAbsorbed(const EventSpellAbsorbed&) = delete;
  EventSpellAbsorbed &operator=(const EventSpellAbsorbed&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellAbsorbed::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSpellAbsorbed::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellAbsorbed::write(FILE* file)
{
  fprintf(file, "", this);
}

