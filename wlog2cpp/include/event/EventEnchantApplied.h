#pragma once

#include "AEventBaseSpell.h"
#include "A2EventEnchant.h"

using namespace types;


class EventEnchantApplied : public AEventBaseSpell, public A2EventEnchant
{

public:

  EventEnchantApplied(WLogFileReader* reader) :
    AEventBaseSpell(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventEnchantApplied() = default;
  EventEnchantApplied(const EventEnchantApplied&) = delete;
  EventEnchantApplied &operator=(const EventEnchantApplied&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventEnchantApplied::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventEnchantApplied::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventEnchantApplied::write(FILE* file)
{
  fprintf(file, "", this);
}

