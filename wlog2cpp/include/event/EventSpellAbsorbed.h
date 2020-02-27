#pragma once

#include "std.h"
#include "AEventBase.h"

using namespace types;

// BASE,                          Player-4701-0094E8DE,"Beemo-Mograine",0x514,0x0, 10193,"Mana Shield",0x40, 570,1593
// BASE, 21333,"Lava Breath",0x4, Player-4701-00B48D7F,"Qopy-Mograine",0x511,0x0,  13033,"Ice Barrier",0x10, 524,722

class EventSpellAbsorbed : public AEventBase
{

protected:

  bool hasBaseSpell;
  uint32_t spellId;
  string_t spellName;
  uint32_t spellSchool;

  AGUID* extraGUID;
  string_t extraName;
  uint32_t extraFlags;
  uint32_t extraRaidFlags;

  uint32_t extraSpellId;
  string_t extraSpellName;
  uint32_t extraSpellSchool;

  uint32_t amount;
  uint32_t p5;

public:

  EventSpellAbsorbed(time_t time, WLogFileReader* reader) :
    AEventBase(time, EventType::SPELL_ABSORBED, reader)
  {
    assert(false);
    // TODO
    
    extraGUID = reader->readGUID();
    extraName = reader->readString();
    extraFlags = reader->readUnsigned(',', 16);
    extraRaidFlags = reader->readUnsigned(',', 16);
    
    extraSpellId = reader->readUnsigned();
    extraSpellName = reader->readString();
    extraSpellSchool = reader->readUnsigned();

    amount = reader->readUnsigned();
    p5 = reader->readUnsigned();
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

