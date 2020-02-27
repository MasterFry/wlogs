#pragma once

#include "AEventSpellAura.h"

using namespace types;

class EventSpellAuraRefresh : public AEventSpellAura
{

public:

  EventSpellAuraRefresh(time_t time, WLogFileReader* reader) :
    AEventSpellAura(time, EventType::SPELL_AURA_REFRESH, reader)
  {
  }

  virtual ~EventSpellAuraRefresh() = default;
  EventSpellAuraRefresh(const EventSpellAuraRefresh&) = delete;
  EventSpellAuraRefresh &operator=(const EventSpellAuraRefresh&) = delete;

};
