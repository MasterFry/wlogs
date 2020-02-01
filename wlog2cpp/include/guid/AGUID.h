#pragma once

#include "IWriteable.h"
#include "GUIDType.h"

using namespace types;

// For players: Player-[server ID]-[player UID] (Example: "Player-970-0002FD64")
// For Unit Type Names: [Unit type]-0-[server ID]-[instance ID]-[zone UID]-[ID]-[spawn UID] 
//   Unit Type Names: "Creature", "Pet", "GameObject", "Vehicle", and "Vignette"
//   (Example: "Creature-0-970-0-11-31146-000136DF91")
// For items: Item-[server ID]-0-[spawn UID] (Example: "Item-970-0-400000076620BFF4")
//   (Please note that this tells you nothing useful about the item, like the ID)

class AGUID : public IWriteable
{

protected:

  AGUID(GUIDType type) :
    type(type)
  {
  }

  virtual ~AGUID() = default;
  AGUID(const AGUID&) = delete;
  AGUID &operator=(const AGUID&) = delete;

  GUIDType type;

public:

  virtual bool operator==(const AGUID& other);
  virtual bool operator!=(const AGUID& other);

};

inline bool AGUID::operator==(const AGUID& other)
{
  return this->type == other.type;
}

inline bool AGUID::operator!=(const AGUID& other)
{
  return this->type != other.type;
}
