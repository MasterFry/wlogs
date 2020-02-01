#include "WLogFileReader.h"
#include "WLogIOException.h"
#include "guids.h"

//---------------------------------------------------------------------------------------------------------------------
string_t WLogFileReader::readValue(char delim)
{
  char c = getChar();
  if(c == delim || c == '\n')
    throw WLogIOException("Field was empty!");

  while(c != delim && c != '\n')
  {
    builder.put(c);
    c = getChar();
  }

  return builder.getString();
}

//---------------------------------------------------------------------------------------------------------------------
ssize_t WLogFileReader::readSigned(char delim)
{
  char c = getChar();
  if(c == delim || c == '\n')
    throw WLogIOException("Field was empty!");
  
  ssize_t value = 0;
  bool negative = false;

  if(c == '-')
  {
    c = getChar();
    negative = true;
  }

  while(c != delim && c != '\n')
  {
    value *= 10;

    if(c >= '0' && c <= '9')
      value += c - '0';
    else
      throw WLogIOException("Invalid value for signed integer!");

    c = getChar();
  }

  return negative ? -value : value;
}

//---------------------------------------------------------------------------------------------------------------------
size_t WLogFileReader::readUnsigned(char delim, size_t base)
{
  size_t value = 0;

  char c = getChar();
  if(c == delim || c == '\n')
    throw WLogIOException("Field was empty!");
  
  if(base == 10)
  {
    while(c != delim && c != '\n')
    {
      value *= 10;

      if(c >= '0' && c <= '9')
        value += c - '0';
      else
        throw WLogIOException("Invalid value for unsigned integer with base 10!");

      c = getChar();
    }
  }
  else if(base == 16)
  {
    if(c == '0')
      c = getChar();
    if(c == 'x' || c == 'X')
      c = getChar();

    while(c != delim && c != '\n')
    {
      value <<= 4;

      if(c >= '0' && c <= '9')
        value += c - '0';
      else if(c >= 'a' && c <= 'f')
        value += c - 'a' + 10;
      else if(c >= 'A' && c <= 'F')
        value += c - 'A' + 10;
      else
        throw WLogIOException("Invalid value for unsigned integer with base 16!");

      c = getChar();
    }
  }
  else
  {
    throw WLogIOException("Invalid base! Only 10 and 16 are supported!");
  }
  
  return value;
}

//---------------------------------------------------------------------------------------------------------------------
float WLogFileReader::readFloat()
{
  ssize_t before = readSigned('.');
  ssize_t after = readSigned(',');

  if(after < 0)
    throw WLogIOException("Invalid value for float!");

  float value = (float) after;
  while(value > 0)
    value /= 10;
  
  return before < 0 ? (float) before - value : (float) before + value;
}

//---------------------------------------------------------------------------------------------------------------------
string_t WLogFileReader::readString()
{
  if(getChar() != '"')
    throw WLogIOException("Invalid value for String!");
  
  string_t value = readValue('"');

  char c = getChar();
  if(c != ',' && c != '\n')
    throw WLogIOException("Invalid value for String!");
  
  return value;
}

//---------------------------------------------------------------------------------------------------------------------
GUIDType WLogFileReader::readGUIDType()
{
  char c = getChar();
  if(c == ',' || c == '\n')
    throw WLogIOException("Field was empty!");

  while(c != '-' && c != ',' && c != '\n')
  {
    builder.put(c);
    c = getChar();
  }

  return getGUIDType(builder.getString());
}

//---------------------------------------------------------------------------------------------------------------------
AGUID* WLogFileReader::readGUID()
{
  switch(readGUIDType())
  {
    case GUIDType::NIL        : return new GUIDNull(this);
    case GUIDType::PLAYER     : return new GUIDPlayer(this);
    case GUIDType::CREATURE   : return new GUIDCreature(this);
    case GUIDType::PET        : return new GUIDPet(this);
    case GUIDType::GAME_OBJECT: return new GUIDGameObject(this);
    case GUIDType::VEHICLE    : return new GUIDVehicle(this);
    case GUIDType::VIGNETTE   : return new GUIDVignette(this);
    case GUIDType::ITEM       : return new GUIDItem(this);
    case GUIDType::CORPSE     : return new GUIDCorpse(this);
  }
}
