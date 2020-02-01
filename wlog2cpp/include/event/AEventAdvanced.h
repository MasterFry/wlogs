#pragma once

#include "AEventBase.h"

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

class AEventAdvanced : public AEventBase
{

protected:

  AEventAdvanced(EventType type, WLogFileReader* reader) :
    AEventBase(type, reader)
  {
    assert(false);
  }

  virtual ~AEventAdvanced() = default;
  AEventAdvanced(const AEventAdvanced&) = delete;
  AEventAdvanced &operator=(const AEventAdvanced&) = delete;

public:

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool AEventAdvanced::operator==(const AEvent& other)
{
  assert(false);
}

inline bool AEventAdvanced::operator!=(const AEvent& other)
{
  assert(false);
}

inline void AEventAdvanced::write(FILE* file)
{
  fprintf(file, "", this);
}

