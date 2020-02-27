#pragma once

#include "AEvent.h"
#include "WLogFileReader.h"

#include <cstdio>

using namespace types;


class A2EventMissed : public IWriteable
{

protected:

  MissType missType;
  bool isOffHand;
  uint32_t amountMissed;
  uint32_t critical;

  A2EventMissed(EventType eventType, WLogFileReader* reader) :
    missType(reader->readMissType()),
    isOffHand(reader->readValue() == "1"),
    amountMissed(0),
    critical(0)
  {
    assert(
      eventType == EventType::SWING_MISSED          ||
      eventType == EventType::RANGE_MISSED          ||
      eventType == EventType::SPELL_MISSED          ||
      eventType == EventType::SPELL_PERIODIC_MISSED ||
      eventType == EventType::DAMAGE_SHIELD_MISSED
    );

    if(this->missType == MissType::ABSORB)
    {
      this->amountMissed = reader->readUnsigned();
      this->critical = reader->readUnsigned();
    }
    else if(this->missType == MissType::RESIST || this->missType == MissType::BLOCK)
    {
      this->amountMissed = reader->readUnsigned();
    }
  }

  virtual ~A2EventMissed() = default;
  A2EventMissed(const A2EventMissed&) = delete;
  A2EventMissed &operator=(const A2EventMissed&) = delete;

public:

  virtual bool operator==(const AEvent& other);
  virtual bool operator!=(const AEvent& other);

  void write(FILE* file) override;

};

inline bool A2EventMissed::operator==(const AEvent& other)
{
  assert(false);
}

inline bool A2EventMissed::operator!=(const AEvent& other)
{
  assert(false);
}
