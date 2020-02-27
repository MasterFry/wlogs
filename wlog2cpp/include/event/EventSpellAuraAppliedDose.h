#pragma once

#include "AEventSpellAuraDose.h"

using namespace types;

class EventSpellAuraAppliedDose : public AEventSpellAuraDose
{

public:

  EventSpellAuraAppliedDose(time_t time, WLogFileReader* reader) :
    AEventSpellAuraDose(time, EventType::SPELL_AURA_APPLIED_DOSE, reader)
  {
  }

  virtual ~EventSpellAuraAppliedDose() = default;
  EventSpellAuraAppliedDose(const EventSpellAuraAppliedDose&) = delete;
  EventSpellAuraAppliedDose &operator=(const EventSpellAuraAppliedDose&) = delete;

};
