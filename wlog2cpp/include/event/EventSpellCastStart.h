#pragma once

#include "AEventBaseSpell.h"

using namespace types;

class EventSpellCastStart : public AEventBaseSpell
{

public:

  EventSpellCastStart(time_t time, WLogFileReader* reader) :
    AEventBaseSpell(time, EventType::SPELL_CAST_START, reader)
  {
  }

  virtual ~EventSpellCastStart() = default;
  EventSpellCastStart(const EventSpellCastStart&) = delete;
  EventSpellCastStart &operator=(const EventSpellCastStart&) = delete;

};
