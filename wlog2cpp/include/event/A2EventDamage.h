#pragma once

#include "AEvent.h"
#include "WLogFileReader.h"

#include <cstdio>

using namespace types;

// 986,896,-1,16,0,0,0,nil,nil,nil
//  1:  amount:
//  2:  ?: 0 - 5000
//  3:  ?: -1 - 2579
//  4:  school: 0 - 127
//  5:  resisted:
//  6:  blocked:
//  7:  absorbed:
//  8:  critical: nil / 1
//  9:  glancing: nil / 1
// 10:  crushing: nil / 1

class A2EventDamage : public IWriteable
{

protected:

  uint32_t amount;
  uint32_t p2;
  int32_t p3;
  uint32_t school;
  int32_t resisted;
  uint32_t blocked;
  uint32_t absorbed;
  bool critical;
  bool glancing;
  bool crushing;

  A2EventDamage(EventType eventType, WLogFileReader* reader) :
    amount(reader->readUnsigned()),
    p2(reader->readUnsigned()),
    p3(reader->readSigned()),
    school(reader->readUnsigned()),
    resisted(reader->readSigned()),
    blocked(reader->readUnsigned()),
    absorbed(reader->readUnsigned()),
    critical(reader->readValue() == "1"),
    glancing(reader->readValue() == "1"),
    crushing(reader->readValue() == "1")
  {
    assert(
      eventType == EventType::ENVIRONMENTAL_DAMAGE  ||
      eventType == EventType::RANGE_DAMAGE          ||
      eventType == EventType::SPELL_DAMAGE          ||
      eventType == EventType::SPELL_PERIODIC_DAMAGE ||
      eventType == EventType::SWING_DAMAGE          ||
      eventType == EventType::SWING_DAMAGE_LANDED   ||
      eventType == EventType::DAMAGE_SPLIT          ||
      eventType == EventType::DAMAGE_SHIELD
    );
  }

  virtual ~A2EventDamage() = default;
  A2EventDamage(const A2EventDamage&) = delete;
  A2EventDamage &operator=(const A2EventDamage&) = delete;

public:

  virtual bool operator==(const AEvent& other);
  virtual bool operator!=(const AEvent& other);

  void write(FILE* file) override;

};

inline bool A2EventDamage::operator==(const AEvent& other)
{
  assert(false);
}

inline bool A2EventDamage::operator!=(const AEvent& other)
{
  assert(false);
}

inline void A2EventDamage::write(FILE* file)
{
  fprintf(file, ",%d,%d,%d,%d,%d,%d,%d,%s,%s,%s",
    this->amount,
    this->p2,
    this->p3,
    this->school,
    this->resisted,
    this->blocked,
    this->absorbed,
    this->critical ? "1" : "nil",
    this->glancing ? "1" : "nil",
    this->crushing ? "1" : "nil"
  );
}

