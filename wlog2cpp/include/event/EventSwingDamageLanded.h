#pragma once

#include "AEventAdvanced.h"
#include "A2EventDamage.h"

using namespace types;


class EventSwingDamageLanded : public AEventAdvanced, public A2EventDamage
{

public:

  EventSwingDamageLanded(WLogFileReader* reader) :
    AEventAdvanced(EventType, reader)
  {
    assert(false);
  }

  virtual ~EventSwingDamageLanded() = default;
  EventSwingDamageLanded(const EventSwingDamageLanded&) = delete;
  EventSwingDamageLanded &operator=(const EventSwingDamageLanded&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSwingDamageLanded::operator==(const AEvent& other)
{
  assert(false);
}

inline bool EventSwingDamageLanded::operator!=(const AEvent& other)
{
  assert(false);
}

inline void EventSwingDamageLanded::write(FILE* file)
{
  fprintf(file, "", this);
}

