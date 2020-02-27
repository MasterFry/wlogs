#pragma once

#include "AEvent.h"

using namespace types;

// 0 : Timestamp
//       1/22 20:39:53.422  
// 1 : Event Name
//       COMBATANT_INFO
// 2 : playerGUID
//       Player-4701-00F19EBB
// 3 : Strength
//       61
// 4 : Agility
//       75
// 5 : Stamina
//       337
// 6 : Intelligence
//       269
// 7 : Spirit
//       172
// 8 : Dodge
//       0 ==> static
// 9 : Parry
//       0 ==> static
// 10 : Block
//       0 ==> static
// 11: CritMelee
//       0 ==> static
// 12: CritRanged
//       0 ==> static
// 13: CritSpell
//       0 ==> static
// 14: Speed
//       0 ==> static
// 15: Lifesteal
//       0 ==> static
// 16: HasteMelee
//       0 ==> static
// 17: HasteRanged
//       0 ==> static
// 18: HasteSpell
//       0 ==> static
// 19: Avoidance
//       0 ==> static
// 20: Mastery
//       0 ==> static
// 21: VersatilityDamageDone
//       0 ==> static
// 22: VersatilityHealingDone
//       0 ==> static
// 23: VersatilityDamageTaken
//       0 ==> static
// 24: Armor
//       1657
// 25: CurrentSpecID
//       0 ==> static
// 26: (Class Talent 1, ...),
//       () ==> static
// 27: (PvP Talent 1, ...),
//       (0,0,0,0) ==> static
// 28: [Artifact Trait ID 1, Trait Effective Level 1, ...],
//       [] ==> static
// 29: [(Equipped Item ID 1,Equipped Item iLvL 1,(Permanent Enchant ID, Temp Enchant ID, On Use Spell Enchant ID),(Bonus List ID 1, ...),(Gem ID 1, Gem iLvL 1, ...)) ...],
//       [(10097,57,(),(),()),(18317,58,(),(),()),(10100,57,(),(),()),(4334,34,(),(),()),(14153,62,(),(),()),(11662,54,(),(),()),(16930,76,(),(),()),(18735,62,(911,0,0),(),()),(16804,66,(929,0,0),(),()),(18407,62,(930,0,0),(),()),(18103,63,(),(),()),(12543,60,(),(),()),(12930,60,(),(),()),(18467,62,(),(),()),(18350,61,(),(),()),(17103,71,(2504,0,0),(),()),(19309,65,(),(),()),(15279,51,(),(),()),(19032,20,(),(),())]
// 30: [Interesting Aura Caster GUID 1, Interesting Aura Spell ID 1, ...]
//       []

class EventCombatantInfo : public AEvent
{

public:

  EventCombatantInfo(time_t time, WLogFileReader* reader) :
    AEvent(time, EventType, reader)
  {
    assert(false);
  }

  virtual ~EventCombatantInfo() = default;
  EventCombatantInfo(const EventCombatantInfo&) = delete;
  EventCombatantInfo &operator=(const EventCombatantInfo&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventCombatantInfo::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventCombatantInfo::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventCombatantInfo::write(FILE* file)
{
  fprintf(file, "", this);
}

