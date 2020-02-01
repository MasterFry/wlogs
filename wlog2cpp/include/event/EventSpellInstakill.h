#pragma once

#include "AEventBaseSpell.h"

using namespace types;


class EventSpellInstakill : public AEventBaseSpell
{

public:

  EventSpellInstakill(WLogFileReader* reader) :
    AEventBaseSpell(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSpellInstakill() = default;
  EventSpellInstakill(const EventSpellInstakill&) = delete;
  EventSpellInstakill &operator=(const EventSpellInstakill&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellInstakill::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSpellInstakill::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellInstakill::write(FILE* file)
{
  fprintf(file, "", this);
}

