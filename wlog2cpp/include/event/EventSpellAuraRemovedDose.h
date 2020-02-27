#pragma once

#include "AEventSpellAuraDose.h"

using namespace types;

class EventSpellAuraRemovedDose : public AEventSpellAuraDose
{

public:

  EventSpellAuraRemovedDose(time_t time, WLogFileReader* reader) :
    AEventSpellAuraDose(time, EventType::SPELL_AURA_REMOVED_DOSE, reader)
  {
  }

  virtual ~EventSpellAuraRemovedDose() = default;
  EventSpellAuraRemovedDose(const EventSpellAuraRemovedDose&) = delete;
  EventSpellAuraRemovedDose &operator=(const EventSpellAuraRemovedDose&) = delete;

};
