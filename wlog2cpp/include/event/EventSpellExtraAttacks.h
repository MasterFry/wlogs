#pragma once

#include "AEventBaseSpell.h"

using namespace types;


class EventSpellExtraAttacks : public AEventBaseSpell
{

public:

  EventSpellExtraAttacks(WLogFileReader* reader) :
    AEventBaseSpell(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSpellExtraAttacks() = default;
  EventSpellExtraAttacks(const EventSpellExtraAttacks&) = delete;
  EventSpellExtraAttacks &operator=(const EventSpellExtraAttacks&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellExtraAttacks::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSpellExtraAttacks::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellExtraAttacks::write(FILE* file)
{
  fprintf(file, "", this);
}

