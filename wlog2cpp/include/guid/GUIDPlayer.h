#pragma once

#include "AGUID.h"
#include "../io/WLogFileReader.h"

// For players: Player-[server ID]-[player UID] (Example: "Player-970-0002FD64")

class GUIDPlayer : public AGUID
{

protected:

  virtual ~GUIDPlayer() = default;
  GUIDPlayer(const GUIDPlayer&) = delete;
  GUIDPlayer &operator=(const GUIDPlayer&) = delete;

  uint32_t serverId;
  uint32_t playerId;

public:

  GUIDPlayer(WLogFileReader* reader) :
    AGUID(GUIDType::PLAYER),
    serverId(reader->readUnsigned('-')),
    playerId(reader->readUnsigned(',', 16))
  {
  }

  void write(FILE* file) override;

  virtual bool operator==(const GUIDPlayer& other);
  virtual bool operator!=(const GUIDPlayer& other);

};

inline void GUIDPlayer::write(FILE* file)
{
  fprintf(file, "Player-%d-%08X", serverId, playerId);
}

inline bool GUIDPlayer::operator==(const GUIDPlayer& other)
{
  return AGUID::operator==(other) && 
        this->serverId == other.serverId && 
        this->playerId == other.playerId;
}

inline bool GUIDPlayer::operator!=(const GUIDPlayer& other)
{
  return AGUID::operator!=(other) || 
        this->serverId != other.serverId || 
        this->playerId != other.playerId;
}
