#pragma once

#include "AEventSpellAura.h"

using namespace types;


class EventSpellAuraRefresh : public AEventSpellAura
{

public:

  EventSpellAuraRefresh(WLogFileReader* reader) :
    AEventSpellAura(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSpellAuraRefresh() = default;
  EventSpellAuraRefresh(const EventSpellAuraRefresh&) = delete;
  EventSpellAuraRefresh &operator=(const EventSpellAuraRefresh&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellAuraRefresh::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSpellAuraRefresh::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSpellAuraRefresh::write(FILE* file)
{
  fprintf(file, "", this);
}

