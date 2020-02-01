#pragma once

#include "AEventBase.h"

using namespace types;


class AEventBaseSpell : public AEventBase
{

protected:

  AEventBaseSpell(EventType type, WLogFileReader* reader) :
    AEventBase(type, reader)
  {
    assert(false);
  }

  virtual ~AEventBaseSpell() = default;
  AEventBaseSpell(const AEventBaseSpell&) = delete;
  AEventBaseSpell &operator=(const AEventBaseSpell&) = delete;

public:

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool AEventBaseSpell::operator==(const AEvent& other)
{
  assert(false);
}

inline bool AEventBaseSpell::operator!=(const AEvent& other)
{
  assert(false);
}

inline void AEventBaseSpell::write(FILE* file)
{
  fprintf(file, "", this);
}

