#pragma once

#include <string>

class GUID
{

public:

  enum class TYPE : unsigned char {
    PLAYER = 0, CREATURE, PET, GAME_OBJECT, VEHICLE, VIGNETTE, ITEM, CORPSE, NIL
  };

  static const std::string NULL_STRING;

  GUID(std::string guid);

  std::string getString() const;

  bool operator==(const GUID& other) const;

  bool operator!=(const GUID& other) const
  {
    return !((*this) == other);
  }

private:

  static const char* TYPE_NAMES[8];

  TYPE type;
  unsigned short serverID;
  unsigned short instanceID;
  unsigned short zoneUID;
  unsigned short ID;
  unsigned long spawnUID;

};