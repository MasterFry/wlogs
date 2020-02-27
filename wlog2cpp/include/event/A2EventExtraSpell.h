#pragma once

#include "std.h"
#include "AEvent.h"
#include "WLogFileReader.h"

#include <cstdio>

using namespace types;


class A2EventExtraSpell : public IWriteable
{

protected:

  uint32_t extraSpellId;
  string_t extraSpellName;
  uint32_t extraSpellSchool;

  A2EventExtraSpell(EventType eventType, WLogFileReader* reader) :
    extraSpellId(reader->readUnsigned()),
    extraSpellName(reader->readString()),
    extraSpellSchool(reader->readUnsigned())
  {
    assert(
      eventType == EventType::SPELL_DISPEL ||
      eventType == EventType::SPELL_INTERRUPT ||
      eventType == EventType::SPELL_AURA_BROKEN_SPELL
    );
  }

  virtual ~A2EventExtraSpell() = default;
  A2EventExtraSpell(const A2EventExtraSpell&) = delete;
  A2EventExtraSpell &operator=(const A2EventExtraSpell&) = delete;

public:

  virtual bool operator==(const AEvent& other);
  virtual bool operator!=(const AEvent& other);

  void write(FILE* file) override;

};

inline bool A2EventExtraSpell::operator==(const AEvent& other)
{
  assert(false);
}

inline bool A2EventExtraSpell::operator!=(const AEvent& other)
{
  assert(false);
}

inline void A2EventExtraSpell::write(FILE* file)
{
  fprintf(file, ",%d,\"%s\",%d",
    this->extraSpellId,
    this->extraSpellName.c_str(),
    this->extraSpellSchool
  );
}

