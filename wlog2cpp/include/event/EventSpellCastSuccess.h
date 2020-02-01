#pragma once

#include "AEventAdvancedSpell.h"

using namespace types;


class EventSpellCastSuccess : public AEventAdvancedSpell
{

public:

  EventSpellCastSuccess(WLogFileReader* reader) :
    AEventAdvancedSpell(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSpellCastSuccess() = default;
  EventSpellCastSuccess(const EventSpellCastSuccess&) = delete;
  EventSpellCastSuccess &operator=(const EventSpellCastSuccess&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellCastSuccess::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSpellCastSuccess::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellCastSuccess::write(FILE* file)
{
  fprintf(file, "", this);
}

