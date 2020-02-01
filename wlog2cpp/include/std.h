#pragma once

#include <assert.h>
#include <string>
#include <cstdlib>

#define likely(x)   __builtin_expect((x), 1)
#define unlikely(x) __builtin_expect((x), 0)

typedef std::string string_t;
