#pragma once

#include "std.h"
#include "AEventBaseSpell.h"

using namespace types;

class EventSpellDurabilityDamage : public AEventBaseSpell
{

protected:

  uint32_t itemId;
  string_t itemName;

public:

  EventSpellDurabilityDamage(time_t time, WLogFileReader* reader) :
    AEventBaseSpell(time, EventType::SPELL_DURABILITY_DAMAGE, reader),
    itemId(reader->readUnsigned()),
    itemName(reader->readString())
  {
  }

  virtual ~EventSpellDurabilityDamage() = default;
  EventSpellDurabilityDamage(const EventSpellDurabilityDamage&) = delete;
  EventSpellDurabilityDamage &operator=(const EventSpellDurabilityDamage&) = delete;

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool EventSpellDurabilityDamage::operator==(const AEvent& other)
{
  return AEventBaseSpell::operator==(other) && this->itemId == ((EventSpellDurabilityDamage*) &other)->itemId;
}

inline bool EventSpellDurabilityDamage::operator!=(const AEvent& other)
{
  return AEventBaseSpell::operator!=(other) || this->itemId != ((EventSpellDurabilityDamage*) &other)->itemId;
}

inline void EventSpellDurabilityDamage::write(FILE* file)
{
  AEventBaseSpell::write(file);
  fprintf(file, ",%d,\"%s\"",
    this->itemId,
    this->itemName
  );
}
