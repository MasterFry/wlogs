#pragma once

#include "AEventSpellAura.h"

using namespace types;

class EventSpellAuraApplied : public AEventSpellAura
{

public:

  EventSpellAuraApplied(time_t time, WLogFileReader* reader) :
    AEventSpellAura(time, EventType::SPELL_AURA_APPLIED, reader)
  {
  }

  virtual ~EventSpellAuraApplied() = default;
  EventSpellAuraApplied(const EventSpellAuraApplied&) = delete;
  EventSpellAuraApplied &operator=(const EventSpellAuraApplied&) = delete;

};
