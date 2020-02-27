#pragma once

#include "AuraType.h"
#include "AEventBaseSpell.h"

using namespace types;

class AEventSpellAuraDose : public AEventBaseSpell
{

protected:

  AuraType auraType;
  uint32_t amount;

  AEventSpellAuraDose(time_t time, EventType eventType, WLogFileReader* reader) :
    AEventBaseSpell(time, eventType, reader),
    auraType(reader->readAuraType()),
    amount(reader->readUnsigned())
  {
    assert(
      eventType == EventType::SPELL_AURA_APPLIED_DOSE ||
      eventType == EventType::SPELL_AURA_REMOVED_DOSE
    );
  }

  virtual ~AEventSpellAuraDose() = default;
  AEventSpellAuraDose(const AEventSpellAuraDose&) = delete;
  AEventSpellAuraDose &operator=(const AEventSpellAuraDose&) = delete;

public:

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool AEventSpellAuraDose::operator==(const AEvent& other)
{
  assert(false);
}

inline bool AEventSpellAuraDose::operator!=(const AEvent& other)
{
  assert(false);
}

inline void AEventSpellAuraDose::write(FILE* file)
{
  AEventBaseSpell::write(file);
  fprintf(file, ",%s,%d",
    getCName(this->auraType),
    this->amount
  );
}
