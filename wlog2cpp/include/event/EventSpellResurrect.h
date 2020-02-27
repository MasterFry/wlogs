#pragma once

#include "AEventBaseSpell.h"

using namespace types;


class EventSpellResurrect : public AEventBaseSpell
{

public:

  EventSpellResurrect(time_t time, WLogFileReader* reader) :
    AEventBaseSpell(time, EventType::SPELL_RESURRECT, reader)
  {
  }

  virtual ~EventSpellResurrect() = default;
  EventSpellResurrect(const EventSpellResurrect&) = delete;
  EventSpellResurrect &operator=(const EventSpellResurrect&) = delete;

};
