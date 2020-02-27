#pragma once

#include "AEvent.h"
#include "WLogFileReader.h"

#include <cstdio>

using namespace types;

// 36.0000,0.0000,0,8319
//  1:  amount
//  2:  overEnergize
//  3:  powerType
//  4:  alternatePowerType

class A2EventEnergize : public IWriteable
{

protected:

  float amount;
  float overEnergize;
  uint32_t powerType;
  uint32_t alternatePowerType;

  A2EventEnergize(EventType eventType, WLogFileReader* reader) :
    amount(reader->readFloat()),
    overEnergize(reader->readFloat()),
    powerType(reader->readUnsigned()),
    alternatePowerType(reader->readUnsigned())
  {
    assert(
      eventType == EventType::SPELL_ENERGIZE ||
      eventType == EventType::SPELL_PERIODIC_ENERGIZE
    );
  }

  virtual ~A2EventEnergize() = default;
  A2EventEnergize(const A2EventEnergize&) = delete;
  A2EventEnergize &operator=(const A2EventEnergize&) = delete;

public:

  virtual bool operator==(const AEvent& other);
  virtual bool operator!=(const AEvent& other);

  void write(FILE* file) override;

};

inline bool A2EventEnergize::operator==(const AEvent& other)
{
  assert(false);
}

inline bool A2EventEnergize::operator!=(const AEvent& other)
{
  assert(false);
}

inline void A2EventEnergize::write(FILE* file)
{
  fprintf(file, ",%.04f,%.04f,%d,%d",
    this->amount,
    this->overEnergize,
    this->powerType,
    this->alternatePowerType
  );
}

