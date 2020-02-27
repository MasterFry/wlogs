#pragma once

#include "guids.h"
#include "AEvent.h"
#include "WLogFileReader.h"

using namespace types;

// 1 :  unitGUID
//       Creature-0-4469-409-26884-11671-0004A8A101
// 2 :  ownerGUID
//       0000000000000000
// 3 :  currHp
//       0
// 4 :  maxHp
//       100 ==> static
// 5 :  attackPower
//       0 ==> static
// 6 :  spellPower
//       0 ==> static
// 7 :  armor
//       0 ==> static
// 8 :  resourceType
//         Enum. PowerType. If there are multiple resource types they are 
//         delimited with a pipe char, e.g. "3|4" for Rogue Energy and ComboPoints.
//       -1 ==> static
// 9 : currResource
//       0 ==> static
// 10: maxResource
//       0 ==> static
// 11: resourceCost
//       0 ==> static
// 12: coord
//       972.03
// 13: coord
//       -948.12
// 14: UiMapID
//       0 ==> static
// 15: facing
//       0.1401
// 16: itemLevel/level
//       61

class A1EventAdvanced : public IWriteable
{

protected:

  AGUID* unitGUID;
  AGUID* ownerGUID;
  uint8_t currHP;
  uint8_t maxHP;
  float coord1;
  float coord2;
  uint32_t mapId;
  float facing;
  uint8_t level;

  A1EventAdvanced(WLogFileReader* reader) :
    unitGUID(reader->readGUID()),       // 1
    ownerGUID(reader->readGUID()),      // 2
    currHP(reader->readUnsigned()),     // 3
    maxHP(reader->readUnsigned())       // 4
  {
    assert(reader->readSigned() == 0);  // 5
    assert(reader->readSigned() == 0);  // 6
    assert(reader->readSigned() == 0);  // 7
    assert(reader->readSigned() == -1); // 8
    assert(reader->readSigned() == 0);  // 9
    assert(reader->readSigned() == 0);  // 10
    assert(reader->readSigned() == 0);  // 11
    coord1 = reader->readFloat();       // 12
    coord2 = reader->readFloat();       // 13
    mapId = reader->readUnsigned();     // 14
    facing = reader->readFloat();       // 15
    level = reader->readUnsigned();     // 16
  }

  virtual ~A1EventAdvanced() = default;
  A1EventAdvanced(const A1EventAdvanced&) = delete;
  A1EventAdvanced &operator=(const A1EventAdvanced&) = delete;

public:

  virtual bool operator==(const AEvent& other);
  virtual bool operator!=(const AEvent& other);

  void write(FILE* file) override;

};

inline bool A1EventAdvanced::operator==(const AEvent& other)
{
  assert(false);
}

inline bool A1EventAdvanced::operator!=(const AEvent& other)
{
  assert(false);
}

inline void A1EventAdvanced::write(FILE* file)
{
  this->unitGUID->write(file);
  this->ownerGUID->write(file);
  fprintf(file, ",%d,%d,0,0,0,-1,0,0,0,%.02f,%.02f,%d,%.04f,%d",
    this->currHP,
    this->maxHP,
    this->coord1,
    this->coord2,
    this->mapId,
    this->facing,
    this->level
  );
}

