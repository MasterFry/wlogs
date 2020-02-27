#pragma once

#include "AEventBase.h"
#include "A1EventAdvanced.h"
#include "A2EventDamage.h"

using namespace types;

class EventSwingDamageLanded : public AEventBase, public A1EventAdvanced, public A2EventDamage
{

public:

  EventSwingDamageLanded(time_t time, WLogFileReader* reader) :
    AEventBase(time, EventType::SWING_DAMAGE_LANDED, reader),
    A1EventAdvanced(reader),
    A2EventDamage(EventType::SWING_DAMAGE_LANDED, reader)
  {
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
  return AEventBase::operator==(other) && A1EventAdvanced::operator==(other) && A2EventDamage::operator==(other);
}

inline bool EventSwingDamageLanded::operator!=(const AEvent& other)
{
  return AEventBase::operator!=(other) || A1EventAdvanced::operator!=(other) || A2EventDamage::operator!=(other);
}

inline void EventSwingDamageLanded::write(FILE* file)
{
  AEventBase::write(file);
  A1EventAdvanced::write(file);
  A2EventDamage::write(file);
}
