#pragma once

#include "AEventAdvancedSpell.h"
#include "A2EventHeal.h"

using namespace types;


class EventSpellHeal : public AEventAdvancedSpell, public A2EventHeal
{

public:

  EventSpellHeal(WLogFileReader* reader) :
    AEventAdvancedSpell(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSpellHeal() = default;
  EventSpellHeal(const EventSpellHeal&) = delete;
  EventSpellHeal &operator=(const EventSpellHeal&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellHeal::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSpellHeal::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellHeal::write(FILE* file)
{
  fprintf(file, "", this);
}

