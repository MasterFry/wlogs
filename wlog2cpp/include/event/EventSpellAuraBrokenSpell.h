#pragma once

#include "AuraType.h"
#include "AEventBaseSpell.h"
#include "A2EventExtraSpell.h"

using namespace types;

class EventSpellAuraBrokenSpell : public AEventBaseSpell, public A2EventExtraSpell
{

protected:

  AuraType auraType;

public:

  EventSpellAuraBrokenSpell(time_t time, WLogFileReader* reader) :
    AEventBaseSpell(time, EventType::SPELL_AURA_BROKEN_SPELL, reader),
    A2EventExtraSpell(EventType::SPELL_AURA_BROKEN_SPELL, reader),
    auraType(reader->readAuraType())
  {
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
  return AEventBaseSpell::operator==(other) &&
         A2EventExtraSpell::operator==(other) &&
         this->auraType == ((EventSpellAuraBrokenSpell*) &other)->auraType;
}

inline bool EventSpellAuraBrokenSpell::operator!=(const AEvent& other)
{
  return AEventBaseSpell::operator!=(other) ||
         A2EventExtraSpell::operator!=(other) ||
         this->auraType != ((EventSpellAuraBrokenSpell*) &other)->auraType;
}

inline void EventSpellAuraBrokenSpell::write(FILE* file)
{
  AEventBaseSpell::write(file);
  A2EventExtraSpell::write(file);
  fprintf(file, ",%s", getCName(this->auraType));
}
