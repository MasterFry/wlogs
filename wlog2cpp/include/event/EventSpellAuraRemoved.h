#pragma once

#include "AEventSpellAura.h"

using namespace types;


class EventSpellAuraRemoved : public AEventSpellAura
{

public:

  EventSpellAuraRemoved(WLogFileReader* reader) :
    AEventSpellAura(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSpellAuraRemoved() = default;
  EventSpellAuraRemoved(const EventSpellAuraRemoved&) = delete;
  EventSpellAuraRemoved &operator=(const EventSpellAuraRemoved&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellAuraRemoved::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSpellAuraRemoved::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellAuraRemoved::write(FILE* file)
{
  fprintf(file, "", this);
}

