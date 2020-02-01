#pragma once

#include "AEventAdvanced.h"

using namespace types;


class AEventAdvancedSpell : public AEventAdvanced
{

protected:

  AEventAdvancedSpell(EventType type, WLogFileReader* reader) :
    AEventAdvanced(type, reader)
  {
    assert(false);
  }

  virtual ~AEventAdvancedSpell() = default;
  AEventAdvancedSpell(const AEventAdvancedSpell&) = delete;
  AEventAdvancedSpell &operator=(const AEventAdvancedSpell&) = delete;

public:

  bool operator==(const AEvent& other) override;
  bool operator!=(const AEvent& other) override;

  void write(FILE* file) override;

};

inline bool AEventAdvancedSpell::operator==(const AEvent& other)
{
  assert(false);
}

inline bool AEventAdvancedSpell::operator!=(const AEvent& other)
{
  assert(false);
}

inline void AEventAdvancedSpell::write(FILE* file)
{
  fprintf(file, "", this);
}

