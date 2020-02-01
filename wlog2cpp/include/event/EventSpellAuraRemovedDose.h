#pragma once

#include "AEventSpellAura.h"

using namespace types;


class EventSpellAuraRemovedDose : public AEventSpellAura
{

public:

  EventSpellAuraRemovedDose(WLogFileReader* reader) :
    AEventSpellAura(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSpellAuraRemovedDose() = default;
  EventSpellAuraRemovedDose(const EventSpellAuraRemovedDose&) = delete;
  EventSpellAuraRemovedDose &operator=(const EventSpellAuraRemovedDose&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellAuraRemovedDose::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSpellAuraRemovedDose::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellAuraRemovedDose::write(FILE* file)
{
  fprintf(file, "", this);
}

