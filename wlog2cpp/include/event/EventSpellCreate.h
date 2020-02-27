#pragma once

#include "AEventBaseSpell.h"

using namespace types;

class EventSpellCreate : public AEventBaseSpell
{

public:

  EventSpellCreate(time_t time, WLogFileReader* reader) :
    AEventBaseSpell(time, EventType::SPELL_CREATE, reader)
  {
  }

  virtual ~EventSpellCreate() = default;
  EventSpellCreate(const EventSpellCreate&) = delete;
  EventSpellCreate &operator=(const EventSpellCreate&) = delete;

};
