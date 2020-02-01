#pragma once

#include "AEventBaseSpell.h"

using namespace types;


class EventSpellAuraBrokenSpell : public AEventBaseSpell
{

public:

  EventSpellAuraBrokenSpell(WLogFileReader* reader) :
    AEventBaseSpell(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSpellAuraBrokenSpell() = default;
  EventSpellAuraBrokenSpell(const EventSpellAuraBrokenSpell&) = delete;
  EventSpellAuraBrokenSpell &operator=(const EventSpellAuraBrokenSpell&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellAuraBrokenSpell::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSpellAuraBrokenSpell::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellAuraBrokenSpell::write(FILE* file)
{
  fprintf(file, "", this);
}

