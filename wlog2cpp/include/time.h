#pragma once

#include "std.h"

typedef struct Time
{
  uint64_t millis    :27; // 24 * 60 * 60 * 1000 = 86.400.000
  uint64_t day       :5 ; // 31
  uint64_t month     :4 ; // 12
  uint64_t __padding :4 ; // pad to 40 bits

  Time(size_t month, size_t day, size_t millis) :
    month(month),
    day(day),
    millis(millis)
  {
  }
  
  Time(size_t month, size_t day, size_t hour, size_t minute, float second) :
    month(month),
    day(day),
    millis((uint64_t) (1000 * second) + 60000 * (minute + 60 * hour))
  {
  }
  
  float second();
  uint8_t minute();
  uint8_t hour();
  uint8_t day();
  uint8_t month();

  const char* string();

} __attribute__((__packed__)) time_t;

inline void operator+=(time_t& a, const ssize_t& millis)
{
  uint32_t time = a.millis + millis;
  assert(time >= 0 && time < 86400000);
  a.millis = time;
}

inline void operator-=(time_t& a, const ssize_t& millis)
{
  uint32_t time = a.millis - millis;
  assert(time >= 0 && time < 86400000);
  a.millis = time;
}

inline time_t operator+(const time_t& a, const ssize_t& millis)
{
  uint32_t time = a.millis + millis;
  assert(time >= 0 && time < 86400000);
  return time_t(a.month, a.day, time);
}

inline time_t operator-(const time_t& a, const ssize_t& millis)
{
  uint32_t time = a.millis - millis;
  assert(time >= 0 && time < 86400000);
  return time_t(a.month, a.day, time);
}

inline float time_t::second()
{
  return (float) (this->millis % 60000);
}

inline uint8_t time_t::minute()
{
  return (uint8_t) (this->millis / 60000);
}

inline uint8_t time_t::hour()
{
  return (uint8_t) (this->millis / 3600000);
}

inline uint8_t time_t::day()
{
  return (uint8_t) this->day;
}

inline uint8_t time_t::month()
{
  return (uint8_t) this->month;
}
