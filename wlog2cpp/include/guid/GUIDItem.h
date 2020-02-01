#pragma once

#include "AGUID.h"
#include "../io/WLogFileReader.h"

// For items: Item-[server ID]-0-[spawn UID] (Example: "Item-970-0-400000076620BFF4")
//   (Please note that this tells you nothing useful about the item, like the ID)

class GUIDItem : public AGUID
{

protected:

  virtual ~GUIDItem() = default;
  GUIDItem(const GUIDItem&) = delete;
  GUIDItem &operator=(const GUIDItem&) = delete;

  uint32_t serverId;
  uint64_t spawnId;

public:

  GUIDItem(WLogFileReader* reader) :
    AGUID(GUIDType::ITEM)
  {
    serverId = reader->readUnsigned('-');
    assert(reader->readUnsigned('-') == 0);
    spawnId = reader->readUnsigned(',', 16);
  }

  void write(FILE* file) override;

  virtual bool operator==(const GUIDItem& other);
  virtual bool operator!=(const GUIDItem& other);

};

inline void GUIDItem::write(FILE* file)
{
  fprintf(file, "Item-%d-0-%016X", serverId, spawnId);
}

inline bool GUIDItem::operator==(const GUIDItem& other)
{
  return AGUID::operator==(other) && 
        this->serverId == other.serverId && 
        this->spawnId == other.spawnId;
}

inline bool GUIDItem::operator!=(const GUIDItem& other)
{
  return AGUID::operator!=(other) || 
        this->serverId != other.serverId || 
        this->spawnId != other.spawnId;
}
