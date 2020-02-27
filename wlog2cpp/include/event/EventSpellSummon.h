#pragma once

#include "AEventBaseSpell.h"

using namespace types;


class EventSpellSummon : public AEventBaseSpell
{

public:

  EventSpellSummon(time_t time, WLogFileReader* reader) :
    AEventBaseSpell(time, EventType::SPELL_SUMMON, reader)
  {
  }

  virtual ~EventSpellSummon() = default;
  EventSpellSummon(const EventSpellSummon&) = delete;
  EventSpellSummon &operator=(const EventSpellSummon&) = delete;

};

