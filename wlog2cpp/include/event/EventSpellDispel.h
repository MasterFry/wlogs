#pragma once

#include "AEventBaseSpell.h"
#include "A2EventExtraSpell.h"

using namespace types;


class EventSpellDispel : public AEventBaseSpell, public A2EventExtraSpell
{

public:

  EventSpellDispel(WLogFileReader* reader) :
    AEventBaseSpell(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSpellDispel() = default;
  EventSpellDispel(const EventSpellDispel&) = delete;
  EventSpellDispel &operator=(const EventSpellDispel&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellDispel::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSpellDispel::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellDispel::write(FILE* file)
{
  fprintf(file, "", this);
}

