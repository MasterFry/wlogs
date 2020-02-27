#pragma once

#include "AEvent.h"
#include "WLogFileReader.h"

#include <cstdio>

using namespace types;

// 296,296,0,0,nil
// 1224,1224,1224,0,nil
//  1:  amount
//  2:  overhealing
//  3:  absorbed
//  4:  ?
//  5:  critical: nil / 1

class A2EventHeal : public IWriteable
{

protected:

  uint32_t amount;
  uint32_t overhealing;
  uint32_t absorbed;
  uint32_t p1;
  bool critical;

  A2EventHeal(EventType eventType, WLogFileReader* reader) :
    amount(reader->readUnsigned()),
    overhealing(reader->readUnsigned()),
    absorbed(reader->readUnsigned()),
    p1(reader->readUnsigned()),
    critical(reader->readValue() == "1")
  {
    assert(
      eventType == EventType::SPELL_HEAL ||
      eventType == EventType::SPELL_PERIODIC_HEAL
    );
  }

  virtual ~A2EventHeal() = default;
  A2EventHeal(const A2EventHeal&) = delete;
  A2EventHeal &operator=(const A2EventHeal&) = delete;

public:

  virtual bool operator==(const AEvent& other);
  virtual bool operator!=(const AEvent& other);

  void write(FILE* file) override;

};

inline bool A2EventHeal::operator==(const AEvent& other)
{
  assert(false);
}

inline bool A2EventHeal::operator!=(const AEvent& other)
{
  assert(false);
}

inline void A2EventHeal::write(FILE* file)
{
  fprintf(file, ",%d,%d,%d,%d,%d",
    this->amount,
    this->overhealing,
    this->absorbed,
    this->p1,
    this->critical
  );
}

