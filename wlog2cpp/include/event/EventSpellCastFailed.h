#pragma once

#include "AEventBaseSpell.h"

using namespace types;


class EventSpellCastFailed : public AEventBaseSpell
{

public:

  EventSpellCastFailed(WLogFileReader* reader) :
    AEventBaseSpell(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSpellCastFailed() = default;
  EventSpellCastFailed(const EventSpellCastFailed&) = delete;
  EventSpellCastFailed &operator=(const EventSpellCastFailed&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellCastFailed::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSpellCastFailed::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellCastFailed::write(FILE* file)
{
  fprintf(file, "", this);
}

