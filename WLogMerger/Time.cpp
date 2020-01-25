
#include "Time.h"

extern Time::TIME_EPSILON = DEFAULT_TIME_EPSILON;

static std::string Time::getString(time_t time)
{
  float second = (float) (time % 60000) / 1000.0f;
  time /= 60000;
  int minute = time % 60;
  time /= 60;
  int hour = time % 24;
  time /= 24;
  MD md = yearDayToMonthAndDay(time);
  
  std::stringstream ss;
  ss << md.month << '/' << md.day << ' ';
  ss.fill('0');
  ss.width(2);
  ss << hour << ':' << minute << ':';
  ss.width(6);
  ss.precision(3);
  ss << second;
  return ss.str();
}

int Time::yearDaysUntilMonth(int month)
{
  bool leap = false; // TODO get leap year
  if(leap)
  {
    switch(month)
    {
      case 1 : return   0;
      case 2 : return  31;
      case 3 : return  60;
      case 4 : return  91;
      case 5 : return 121;
      case 6 : return 152;
      case 7 : return 182;
      case 8 : return 213;
      case 9 : return 244;
      case 10: return 274;
      case 11: return 305;
      case 12: return 335;
    }
  }
  else
  {
    switch(month)
    {
      case 1 : return   0;
      case 2 : return  31;
      case 3 : return  59;
      case 4 : return  90;
      case 5 : return 120;
      case 6 : return 151;
      case 7 : return 181;
      case 8 : return 212;
      case 9 : return 243;
      case 10: return 273;
      case 11: return 304;
      case 12: return 334;
    }
  }
}

Time::MD Time::yearDayToMonthAndDay(int yDay)
{
  bool leap = false; // TODO get leap year
  if(leap)
  {
    if(yDay >= 335) return { .day = yDay - 335, .month = 12 };
    if(yDay >= 305) return { .day = yDay - 305, .month = 11 };
    if(yDay >= 274) return { .day = yDay - 274, .month = 10 };
    if(yDay >= 244) return { .day = yDay - 244, .month =  9 };
    if(yDay >= 213) return { .day = yDay - 213, .month =  8 };
    if(yDay >= 182) return { .day = yDay - 182, .month =  7 };
    if(yDay >= 152) return { .day = yDay - 152, .month =  6 };
    if(yDay >= 121) return { .day = yDay - 121, .month =  5 };
    if(yDay >=  91) return { .day = yDay -  91, .month =  4 };
    if(yDay >=  60) return { .day = yDay -  60, .month =  3 };
    if(yDay >=  31) return { .day = yDay -  31, .month =  2 };
    return { .day = yDay, .month = 1 };
  }
  else
  {
    if(yDay >= 334) return { .day = yDay - 334, .month = 12 };
    if(yDay >= 304) return { .day = yDay - 304, .month = 11 };
    if(yDay >= 273) return { .day = yDay - 273, .month = 10 };
    if(yDay >= 243) return { .day = yDay - 243, .month =  9 };
    if(yDay >= 212) return { .day = yDay - 212, .month =  8 };
    if(yDay >= 181) return { .day = yDay - 181, .month =  7 };
    if(yDay >= 151) return { .day = yDay - 151, .month =  6 };
    if(yDay >= 120) return { .day = yDay - 120, .month =  5 };
    if(yDay >=  90) return { .day = yDay -  90, .month =  4 };
    if(yDay >=  59) return { .day = yDay -  59, .month =  3 };
    if(yDay >=  31) return { .day = yDay -  31, .month =  2 };
    return { .day = yDay, .month = 1 };
  }
}