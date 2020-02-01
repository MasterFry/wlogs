#pragma once

#include "AEventBaseSpell.h"

using namespace types;


class EventSpellAuraBroken : public AEventBaseSpell
{

public:

  EventSpellAuraBroken(WLogFileReader* reader) :
    AEventBaseSpell(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSpellAuraBroken() = default;
  EventSpellAuraBroken(const EventSpellAuraBroken&) = delete;
  EventSpellAuraBroken &operator=(const EventSpellAuraBroken&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellAuraBroken::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSpellAuraBroken::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellAuraBroken::write(FILE* file)
{
  fprintf(file, "", this);
}

