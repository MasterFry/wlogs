#pragma once

#include "AEventBaseSpell.h"

using namespace types;

class EventSpellInstakill : public AEventBaseSpell
{

public:

  EventSpellInstakill(time_t time, WLogFileReader* reader) :
    AEventBaseSpell(time, EventType::SPELL_INSTAKILL, reader)
  {
  }

  virtual ~EventSpellInstakill() = default;
  EventSpellInstakill(const EventSpellInstakill&) = delete;
  EventSpellInstakill &operator=(const EventSpellInstakill&) = delete;

};
