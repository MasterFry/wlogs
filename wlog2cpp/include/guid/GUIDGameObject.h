#pragma once

#include "AGUIDUnitType.h"

class GUIDGameObject : public AGUIDUnitType
{

protected:

  virtual ~GUIDGameObject() = default;
  GUIDGameObject(const GUIDGameObject&) = delete;
  GUIDGameObject &operator=(const GUIDGameObject&) = delete;


public:

  GUIDGameObject(WLogFileReader* reader) :
    AGUIDUnitType(GUIDType::GAME_OBJECT, reader)
  {
  }

};
