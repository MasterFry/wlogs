#pragma once

#include "AEventBaseSpell.h"

using namespace types;


class EventSpellCastStart : public AEventBaseSpell
{

public:

  EventSpellCastStart(WLogFileReader* reader) :
    AEventBaseSpell(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSpellCastStart() = default;
  EventSpellCastStart(const EventSpellCastStart&) = delete;
  EventSpellCastStart &operator=(const EventSpellCastStart&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellCastStart::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSpellCastStart::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellCastStart::write(FILE* file)
{
  fprintf(file, "", this);
}

