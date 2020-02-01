#pragma once

#include "AEventSpellAura.h"

using namespace types;


class EventSpellAuraAppliedDose : public AEventSpellAura
{

public:

  EventSpellAuraAppliedDose(WLogFileReader* reader) :
    AEventSpellAura(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSpellAuraAppliedDose() = default;
  EventSpellAuraAppliedDose(const EventSpellAuraAppliedDose&) = delete;
  EventSpellAuraAppliedDose &operator=(const EventSpellAuraAppliedDose&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellAuraAppliedDose::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSpellAuraAppliedDose::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellAuraAppliedDose::write(FILE* file)
{
  fprintf(file, "", this);
}

