#pragma once

#include "AEventBase.h"
#include "A1EventAdvanced.h"
#include "A2EventDamage.h"

using namespace types;

class EventSwingDamage : public AEventBase, public A1EventAdvanced, public A2EventDamage
{

public:

  EventSwingDamage(time_t time, WLogFileReader* reader) :
    AEventBase(time, EventType::SWING_DAMAGE, reader),
    A1EventAdvanced(reader),
    A2EventDamage(EventType::SWING_DAMAGE, reader)
  {
  }

  virtual ~EventSwingDamage() = default;
  EventSwingDamage(const EventSwingDamage&) = delete;
  EventSwingDamage &operator=(const EventSwingDamage&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSwingDamage::operator==(const AEvent& other)
{
  return AEventBase::operator==(other) && A1EventAdvanced::operator==(other) && A2EventDamage::operator==(other);
}

inline bool EventSwingDamage::operator!=(const AEvent& other)
{
  return AEventBase::operator!=(other) || A1EventAdvanced::operator!=(other) || A2EventDamage::operator!=(other);
}

inline void EventSwingDamage::write(FILE* file)
{
  AEventBase::write(file);
  A1EventAdvanced::write(file);
  A2EventDamage::write(file);
}
