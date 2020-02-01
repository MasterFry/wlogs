#pragma once

#include "AEventBaseSpell.h"

using namespace types;


class EventSpellCreate : public AEventBaseSpell
{

public:

  EventSpellCreate(WLogFileReader* reader) :
    AEventBaseSpell(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSpellCreate() = default;
  EventSpellCreate(const EventSpellCreate&) = delete;
  EventSpellCreate &operator=(const EventSpellCreate&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellCreate::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSpellCreate::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellCreate::write(FILE* file)
{
  fprintf(file, "", this);
}

