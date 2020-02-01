#pragma once

#include "AGUID.h"
#include "WLogFileReader.h"

// For Unit Type Names: [Unit type]-0-[server ID]-[instance ID]-[zone UID]-[ID]-[spawn UID] 
//   Unit Type Names: "Creature", "Pet", "GameObject", "Vehicle", and "Vignette"
//   (Example: "Creature-0-970-0-11-31146-000136DF91")

class AGUIDUnitType : public AGUID
{

protected:

  AGUIDUnitType(GUIDType type, WLogFileReader* reader) :
    AGUID(type)
  {
    assert(
      type == GUIDType::CORPSE ||
      type == GUIDType::CREATURE ||
      type == GUIDType::GAME_OBJECT ||
      type == GUIDType::PET ||
      type == GUIDType::VEHICLE ||
      type == GUIDType::VIGNETTE
    );
    assert(reader->readUnsigned('-') == 0);
    serverId   = reader->readUnsigned('-');
    instanceId = reader->readUnsigned('-');
    zoneId     = reader->readUnsigned('-');
    id         = reader->readUnsigned('-');
    spawnId    = reader->readUnsigned(',', 16);
  }

  virtual ~AGUIDUnitType() = default;
  AGUIDUnitType(const AGUIDUnitType&) = delete;
  AGUIDUnitType &operator=(const AGUIDUnitType&) = delete;

  uint32_t serverId;
  uint32_t instanceId;
  uint32_t zoneId;
  uint32_t id;
  uint64_t spawnId;

public:

  void write(FILE* file) override;

  virtual bool operator==(const AGUIDUnitType& other);
  virtual bool operator!=(const AGUIDUnitType& other);

};

inline void AGUIDUnitType::write(FILE* file)
{
  fprintf(file, "%s-0-%d-%d-%d-%d-%016X", getCName(type), serverId, instanceId, zoneId, id, spawnId);
}

inline bool AGUIDUnitType::operator==(const AGUIDUnitType& other)
{
  return AGUID::operator==(other) && 
        this->serverId == other.serverId && 
        this->instanceId == other.instanceId && 
        this->zoneId == other.zoneId && 
        this->id == other.id && 
        this->spawnId == other.spawnId;
}

inline bool AGUIDUnitType::operator!=(const AGUIDUnitType& other)
{
  return AGUID::operator!=(other) || 
        this->serverId != other.serverId || 
        this->instanceId != other.instanceId || 
        this->zoneId != other.zoneId || 
        this->id != other.id || 
        this->spawnId != other.spawnId;
}
    