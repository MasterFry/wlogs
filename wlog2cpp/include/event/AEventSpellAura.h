#pragma once

#include "AuraType.h"
#include "AEventBaseSpell.h"

using namespace types;

class AEventSpellAura : public AEventBaseSpell
{

protected:

  AuraType auraType;

  AEventSpellAura(time_t time, EventType eventType, WLogFileReader* reader) :
    AEventBaseSpell(time, eventType, reader),
    auraType(reader->readAuraType())
  {
    assert(
      eventType == EventType::SPELL_AURA_APPLIED ||
      eventType == EventType::SPELL_AURA_REMOVED ||
      eventType == EventType::SPELL_AURA_REFRESH
    );
  }

  virtual ~AEventSpellAura() = default;
  AEventSpellAura(const AEventSpellAura&) = delete;
  AEventSpellAura &operator=(const AEventSpellAura&) = delete;

public:

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool AEventSpellAura::operator==(const AEvent& other)
{
  assert(false);
}

inline bool AEventSpellAura::operator!=(const AEvent& other)
{
  assert(false);
}

inline void AEventSpellAura::write(FILE* file)
{
  AEventBaseSpell::write(file);
  fprintf(file, ",%s", getCName(this->auraType));
}
