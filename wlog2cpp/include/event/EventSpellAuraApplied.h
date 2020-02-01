#pragma once

#include "AEventSpellAura.h"

using namespace types;


class EventSpellAuraApplied : public AEventSpellAura
{

public:

  EventSpellAuraApplied(WLogFileReader* reader) :
    AEventSpellAura(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSpellAuraApplied() = default;
  EventSpellAuraApplied(const EventSpellAuraApplied&) = delete;
  EventSpellAuraApplied &operator=(const EventSpellAuraApplied&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellAuraApplied::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSpellAuraApplied::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellAuraApplied::write(FILE* file)
{
  fprintf(file, "", this);
}

