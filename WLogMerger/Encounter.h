#pragma once

#include "Time.h"
#include <vector>
#include <map>

class GUID;
class Event;

class Encounter
{

public:

  Encounter();

private:

  time_t timeStart;
  time_t timeEnd;
  unsigned long ID;
  std::string name;
  unsigned char difficultyID;
  unsigned char groupSize;
  std::string unknownStart;
  std::string unknownEnd;
  std::vector<Event*> events;
  // std::map<GUID*, 

};