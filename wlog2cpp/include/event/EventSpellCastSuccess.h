#pragma once

#include "AEventAdvancedSpell.h"

using namespace types;

class EventSpellCastSuccess : public AEventAdvancedSpell
{

public:

  EventSpellCastSuccess(time_t time, WLogFileReader* reader) :
    AEventAdvancedSpell(time, EventType::SPELL_CAST_SUCCESS, reader)
  {
  }

  virtual ~EventSpellCastSuccess() = default;
  EventSpellCastSuccess(const EventSpellCastSuccess&) = delete;
  EventSpellCastSuccess &operator=(const EventSpellCastSuccess&) = delete;

};
