#pragma once

#include "AEventBaseSpell.h"

using namespace types;


class EventSpellSummon : public AEventBaseSpell
{

public:

  EventSpellSummon(WLogFileReader* reader) :
    AEventBaseSpell(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSpellSummon() = default;
  EventSpellSummon(const EventSpellSummon&) = delete;
  EventSpellSummon &operator=(const EventSpellSummon&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellSummon::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSpellSummon::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellSummon::write(FILE* file)
{
  fprintf(file, "", this);
}

