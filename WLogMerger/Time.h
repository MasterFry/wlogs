#pragma once

#include <string>
#include <sstream>

#define DEFAULT_TIME_EPSILON 5000

typedef unsigned int time_t;

class Time
{

private:

  struct MD
  {
    int day;
    int month;
  }

  static time_t TIME_EPSILON;

public:

  static setEpsilon(time_t epsilon)
  {
    TIME_EPSILON = epsilon;
  }
  
  static resetEpsilon()
  {
    TIME_EPSILON = DEFAULT_TIME_EPSILON;
  }

  static time_t get(int month, int day, int hour, int minute, float second)
  {
    return (time_t) (second * 1000) + (time_t) (60000 * (minute + 60 * (hour + 24 * (day + yearDaysUntilMonth(month)))));
  }

  static int compare(time_t a, time_t b)
  {
    if(a + TIME_EPSILON < b) return -1;
    if(a > b + TIME_EPSILON) return 1;
    return 0;
  }

  static std::string getString(time_t time);

  static int yearDaysUntilMonth(int month);
  static MD yearDayToMonthAndDay(int yDay);

};