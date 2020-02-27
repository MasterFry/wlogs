#pragma once

#include "AEventBaseSpell.h"

using namespace types;

class EventSpellExtraAttacks : public AEventBaseSpell
{

protected:

  uint32_t amount;

public:

  EventSpellExtraAttacks(time_t time, WLogFileReader* reader) :
    AEventBaseSpell(time, EventType::SPELL_EXTRA_ATTACKS, reader),
    amount(reader->readUnsigned())
  {
  }

  virtual ~EventSpellExtraAttacks() = default;
  EventSpellExtraAttacks(const EventSpellExtraAttacks&) = delete;
  EventSpellExtraAttacks &operator=(const EventSpellExtraAttacks&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellExtraAttacks::operator==(const AEvent& other)
{
  return AEventBaseSpell::operator==(other) && this->amount == ((EventSpellExtraAttacks*) &other)->amount;
}

inline bool EventSpellExtraAttacks::operator!=(const AEvent& other)
{
  return AEventBaseSpell::operator!=(other) || this->amount != ((EventSpellExtraAttacks*) &other)->amount;
}

inline void EventSpellExtraAttacks::write(FILE* file)
{
  AEventBaseSpell::write(file);
  fprintf(file, ",%d", this->amount);
}

