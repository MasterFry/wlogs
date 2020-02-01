#pragma once

#include "AGUIDUnitType.h"

class GUIDVehicle : public AGUIDUnitType
{

protected:

  virtual ~GUIDVehicle() = default;
  GUIDVehicle(const GUIDVehicle&) = delete;
  GUIDVehicle &operator=(const GUIDVehicle&) = delete;


public:

  GUIDVehicle(WLogFileReader* reader) :
    AGUIDUnitType(GUIDType::VEHICLE, reader)
  {
  }

};
