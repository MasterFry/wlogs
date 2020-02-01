#pragma once

#include "AEventBaseSpell.h"

using namespace types;


class AEventSpellAura : public AEventBaseSpell
{

protected:

  AEventSpellAura(EventType type, WLogFileReader* reader) :
    AEventBaseSpell(type, reader)
  {
    assert(false);
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
  fprintf(file, "", this);
}

