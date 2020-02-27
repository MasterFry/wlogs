#pragma once

#include "AuraType.h"
#include "AEventBaseSpell.h"
#include "A2EventExtraSpell.h"

using namespace types;

class EventSpellDispel : public AEventBaseSpell, public A2EventExtraSpell
{

protected:

  AuraType auraType;

public:

  EventSpellDispel(time_t time, WLogFileReader* reader) :
    AEventBaseSpell(time, EventType::SPELL_DISPEL, reader),
    A2EventExtraSpell(EventType::SPELL_DISPEL, reader),
    auraType(reader->readAuraType())
  {
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
  return AEventBaseSpell::operator==(other) && 
         A2EventExtraSpell::operator==(other) && 
         this->auraType == ((EventSpellDispel*) &other)->auraType;
}

inline bool EventSpellDispel::operator!=(const AEvent& other)
{
  return AEventBaseSpell::operator!=(other) || 
         A2EventExtraSpell::operator!=(other) || 
         this->auraType != ((EventSpellDispel*) &other)->auraType;
}

inline void EventSpellDispel::write(FILE* file)
{
  AEventBaseSpell::write(file);
  A2EventExtraSpell::write(file);
  fprintf(file, ",%s", getCName(this->auraType));
}
