#pragma once

#include "AEvent.h"
#include "WLogFileReader.h"

#include <cstdio>

using namespace types;

// amount, powerType, extraAmount ?

class A2EventDrain : public IWriteable
{

protected:

  uint32_t amount;
  uint32_t powerType;
  uint32_t extraAmount;
  uint32_t p6;

  A2EventDrain(EventType eventType, WLogFileReader* reader) :
    amount(reader->readUnsigned()),
    powerType(reader->readUnsigned()),
    extraAmount(reader->readUnsigned()),
    p6(reader->readUnsigned())
  {
    assert(
      eventType == EventType::SPELL_DRAIN ||
      eventType == EventType::SPELL_PERIODIC_DRAIN ||
      eventType == EventType::SPELL_PERIODIC_LEECH
    );
  }

  virtual ~A2EventDrain() = default;
  A2EventDrain(const A2EventDrain&) = delete;
  A2EventDrain &operator=(const A2EventDrain&) = delete;

public:

  virtual bool operator==(const AEvent& other);
  virtual bool operator!=(const AEvent& other);

  void write(FILE* file) override;

};

inline bool A2EventDrain::operator==(const AEvent& other)
{
  assert(false);
}

inline bool A2EventDrain::operator!=(const AEvent& other)
{
  assert(false);
}

inline void A2EventDrain::write(FILE* file)
{
  fprintf(file, ",%d,%d,%d,%d",
    this->amount,
    this->powerType,
    this->extraAmount,
    this->p6
  );
}

