#pragma once

#include "AEventBase.h"

using namespace types;


class AEventBaseSpell : public AEventBase
{

protected:

  uint32_t spellId;
  string_t spellName;
  uint32_t spellSchool;

  AEventBaseSpell(time_t time, EventType eventType, WLogFileReader* reader) :
    AEventBase(time, eventType, reader),
    spellId(reader->readUnsigned()),
    spellName(reader->readString()),
    spellSchool(reader->readUnsigned(',', 16))
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
  AEventBase::write(file);
  fprintf(file, ",%d,\"%s\",%d",
    this->spellId,
    this->spellName,
    this->spellSchool
  );
}

