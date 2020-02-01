#pragma once

#include "AEventBaseSpell.h"

using namespace types;


class EventSpellResurrect : public AEventBaseSpell
{

public:

  EventSpellResurrect(WLogFileReader* reader) :
    AEventBaseSpell(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSpellResurrect() = default;
  EventSpellResurrect(const EventSpellResurrect&) = delete;
  EventSpellResurrect &operator=(const EventSpellResurrect&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellResurrect::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSpellResurrect::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellResurrect::write(FILE* file)
{
  fprintf(file, "", this);
}

