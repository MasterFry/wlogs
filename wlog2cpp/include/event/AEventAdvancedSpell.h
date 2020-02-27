#pragma once

#include "AEventBaseSpell.h"
#include "A1EventAdvanced.h"

using namespace types;


class AEventAdvancedSpell : public AEventBaseSpell, public A1EventAdvanced
{

protected:

  AEventAdvancedSpell(time_t time, EventType eventType, WLogFileReader* reader) :
    AEventBaseSpell(time, eventType, reader),
    A1EventAdvanced(reader)
  {
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
  AEventBaseSpell::write(file);
  A1EventAdvanced::write(file);
}

