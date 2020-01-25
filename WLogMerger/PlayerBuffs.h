#pragma once

#include <map>
#include <string>
#include "Time.h"
#include "GUID.h"

using std::string;

typedef unsigned int spellid_t;

class PlayerBuffs
{

private:

  struct BuffData
  {
    time_t time;
    string caster;
  };

  std::map<spellid_t, BuffData> buffs;

  PlayerBuffs(const PlayerBuffs& other)
  {
    
  }

public:

  PlayerBuffs() = default;
  ~PlayerBuffs() = default;

  void set(spellid_t spellid, time_t time, string caster)
  {
    if(buffs[spellid].time < time)
      buffs[spellid] = BuffData{ .time = time, .caster = caster };
  }

  void unsetAll(time_t time)
  {
    for(auto it = buffs.begin(); it != buffs.end(); ++it)
    {
      it->second.time = time;
      it->second.caster = GUID::NULL_STRING;
    }
  }

  void merge(PlayerBuffs* other)
  {
    for(auto other_it = other->buffs.begin(); other_it != other->buffs.end(); ++other_it)
    {
      auto it = buffs.find(other_it->first);
      if(it == buffs.end())
      {
        buffs.insert(std::pair<spellid_t, BuffData>(
          other_it->first, BuffData{ .time = other_it->second.time, .caster = other_it->second.caster }
        ));
      }
      else if(it->second.time < other_it->second.time)
      {
        it->second.time = other_it->second.time;
        it->second.caster = other_it->second.caster;
      }
    }
  }

};
