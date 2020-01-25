#include "GUID.h"
#include "ParameterException.h"
#include <sstream>

extern const std::string GUID::NULL_STRING("0000000000000000");
extern const char* GUID::TYPE_NAMES[8] = {
  "Player", "Creature", "Pet", "GameObject", "Vehicle", "Vignette", "Item", "Corpse"
};

GUID::GUID(std::string guid)
{
  switch(guid[0])
  {
    case 'P': type = guid[1] == 'l' ? TYPE::PLAYER : TYPE::PET; break;
    case 'C': type = guid[1] == 'r' ? TYPE::CREATURE : TYPE::CORPSE; break;
    case 'G': type = TYPE::GAME_OBJECT; break;
    case 'V': type = guid[1] == 'e' ? TYPE::VEHICLE : TYPE::VIGNETTE; break;
    case 'I': type = TYPE::ITEM; break;
    case '0': if(guid == NULL_STRING) { type = TYPE::NIL; break; } // else -> fall through
    default: throw ParameterException("Invalid GUID", guid);
  }

  size_t index;
  if(type == TYPE::PLAYER)
  {
    serverID = std::stoi(guid.substr(guid.find('-') + 1), &index, 16);
    spawnUID = std::stoi(guid.substr(index + 1), &index, 16);
    if(index != guid.length())
      throw ParameterException("Invalid GUID", guid);
  }
  else if(type == TYPE::ITEM)
  {
    serverID = std::stoi(guid.substr(guid.find('-') + 1), &index, 16);
    if(guid[index] != '-' || guid[index + 1] != '0' || guid[index + 2] != '-')
      throw ParameterException("Invalid GUID", guid);
    spawnUID = std::stoi(guid.substr(index + 3), &index, 16);
    if(index != guid.length())
      throw ParameterException("Invalid GUID", guid);
  }
  else if(type != TYPE::NIL)
  {
    index = guid.find('-');
    if(guid[index + 1] != '0' || guid[index + 2] != '-')
      throw ParameterException("Invalid GUID", guid);
    serverID   = std::stoi(guid.substr(index + 3), &index, 16);
    instanceID = std::stoi(guid.substr(index + 1), &index, 16);
    zoneUID    = std::stoi(guid.substr(index + 1), &index, 16);
    ID         = std::stoi(guid.substr(index + 1), &index, 16);
    spawnUID   = std::stoi(guid.substr(index + 1), &index, 16);
    if(index != guid.length())
      throw ParameterException("Invalid GUID", guid);
  }
}

std::string GUID::getString() const
{
  if(type == TYPE::NIL)
    return NULL_STRING;
    
  std::stringstream ss;
  ss.fill('0');
  ss.setf(std::ios_base::hex , std::ios_base::basefield);
  ss << TYPE_NAMES[(int) type];

  if(type == TYPE::PLAYER)
  {
    ss << '-' << serverID << '-';
    ss.width(8);
    ss << spawnUID;
  }
  else if(type == TYPE::ITEM)
  {
    ss << '-' << serverID << "-0-";
    ss.width(16);
    ss << spawnUID;
  }
  else
  {
    ss << "-0-" << serverID << '-' << instanceID << '-' << zoneUID << '-' << ID << '-';
    ss.width(10);
    ss << spawnUID;
  }

  return ss.str();
}

bool GUID::operator==(const GUID& other) const
{
  if(type != other.type) return false;
  if(type == TYPE::NIL) return true;
  if(type == TYPE::PLAYER || type == TYPE::ITEM) return spawnUID == other.spawnUID;
  return spawnUID == other.spawnUID && 
         instanceID == other.instanceID && 
         zoneUID == other.zoneUID && 
         ID == other.ID;
}
