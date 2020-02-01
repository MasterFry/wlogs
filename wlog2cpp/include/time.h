#pragma once

#include "std.h"

#include <cstdint>

typedef struct asdf
{
  uint64_t second :1;
  uint64_t minute :1;
  uint64_t hour   :1;
  uint64_t day    :1;
  uint64_t month  :1;
} __attribute__((__packed__));

