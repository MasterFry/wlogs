#pragma once

#include "AuraType.h"
#include "AEventBaseSpell.h"

using namespace types;

class EventSpellAuraBroken : public AEventBaseSpell
{

protected:

  AuraType auraType;

public:

  EventSpellAuraBroken(time_t time, WLogFileReader* reader) :
    AEventBaseSpell(time, EventType::SPELL_AURA_BROKEN, reader),
    auraType(reader->readAuraType())
  {
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
  return AEventBaseSpell::operator==(other) && this->auraType == ((EventSpellAuraBroken*) &other)->auraType;
}

inline bool EventSpellAuraBroken::operator!=(const AEvent& other)
{
  return AEventBaseSpell::operator!=(other) || this->auraType != ((EventSpellAuraBroken*) &other)->auraType;
}

inline void EventSpellAuraBroken::write(FILE* file)
{
  AEventBaseSpell::write(file);
  fprintf(file, ",%s", getCName(this->auraType));
}
