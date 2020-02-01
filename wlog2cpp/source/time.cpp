#include "time.h"

#include <sstream>
#include <iomanip>

const char* time_t::string()
{
  std::ostringstream ss;
  // 1/29 21:23:27.402
  ss << std::setw(1) << this->month << '/' << this->day << ' ';
  ss << std::setw(2) << std::setfill('0');
  ss << this->hour() << ':' << this->minute() << ':';
  ss << std::setw(6) << std::setprecision(3) << this->second();

  return ss.str().c_str();
}
