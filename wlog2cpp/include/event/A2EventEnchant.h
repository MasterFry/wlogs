#pragma once

#include "std.h"
#include "AEvent.h"
#include "WLogFileReader.h"

#include <cstdio>

using namespace types;

//  1:  spellName
//  2:  itemId
//  3:  itemName

class A2EventEnchant : public IWriteable
{

protected:

  string_t spellName;
  uint32_t itemId;
  string_t itemName;

  A2EventEnchant(EventType eventType, WLogFileReader* reader) :
    spellName(reader->readString()),
    itemId(reader->readUnsigned()),
    itemName(reader->readString())
  {
    assert(
      eventType == EventType::ENCHANT_APPLIED ||
      eventType == EventType::ENCHANT_REMOVED
    );
  }

  virtual ~A2EventEnchant() = default;
  A2EventEnchant(const A2EventEnchant&) = delete;
  A2EventEnchant &operator=(const A2EventEnchant&) = delete;

public:

  virtual bool operator==(const AEvent& other);
  virtual bool operator!=(const AEvent& other);

  void write(FILE* file) override;

};

inline bool A2EventEnchant::operator==(const AEvent& other)
{
  assert(false);
}

inline bool A2EventEnchant::operator!=(const AEvent& other)
{
  assert(false);
}

inline void A2EventEnchant::write(FILE* file)
{
  fprintf(file, ",\"%s\",%d,\"%s\"", 
    this->spellName.c_str(), 
    this->itemId, 
    this->itemName.c_str()
  );
}

