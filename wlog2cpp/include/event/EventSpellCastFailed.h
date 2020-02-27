#pragma once

#include "std.h"
#include "AEventBaseSpell.h"

using namespace types;

class EventSpellCastFailed : public AEventBaseSpell
{

protected:

  string_t failedType;

public:

  EventSpellCastFailed(time_t time, WLogFileReader* reader) :
    AEventBaseSpell(time, EventType::SPELL_CAST_FAILED, reader),
    failedType(reader->readString())
  {
  }

  virtual ~EventSpellCastFailed() = default;
  EventSpellCastFailed(const EventSpellCastFailed&) = delete;
  EventSpellCastFailed &operator=(const EventSpellCastFailed&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellCastFailed::operator==(const AEvent& other)
{
  return AEventBaseSpell::operator==(other) && this->failedType == ((EventSpellCastFailed*) &other)->failedType;
}

inline bool EventSpellCastFailed::operator!=(const AEvent& other)
{
  return AEventBaseSpell::operator!=(other) || this->failedType != ((EventSpellCastFailed*) &other)->failedType;
}

inline void EventSpellCastFailed::write(FILE* file)
{
  AEventBaseSpell::write(file);
  fprintf(file, ",\"%s\"", failedType);
}
