#pragma once

#include "AEventBaseSpell.h"
#include "A2EventEnchant.h"

using namespace types;


class EventEnchantRemoved : public AEventBaseSpell, public A2EventEnchant
{

public:

  EventEnchantRemoved(WLogFileReader* reader) :
    AEventBaseSpell(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventEnchantRemoved() = default;
  EventEnchantRemoved(const EventEnchantRemoved&) = delete;
  EventEnchantRemoved &operator=(const EventEnchantRemoved&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventEnchantRemoved::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventEnchantRemoved::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventEnchantRemoved::write(FILE* file)
{
  fprintf(file, "", this);
}

