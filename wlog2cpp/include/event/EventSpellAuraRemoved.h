#pragma once

#include "AEventSpellAura.h"

using namespace types;

class EventSpellAuraRemoved : public AEventSpellAura
{

public:

  EventSpellAuraRemoved(time_t time, WLogFileReader* reader) :
    AEventSpellAura(time, EventType::SPELL_AURA_REMOVED, reader)
  {
  }

  virtual ~EventSpellAuraRemoved() = default;
  EventSpellAuraRemoved(const EventSpellAuraRemoved&) = delete;
  EventSpellAuraRemoved &operator=(const EventSpellAuraRemoved&) = delete;

};
