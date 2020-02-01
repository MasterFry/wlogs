#pragma once

#include <assert.h>
#include <cstdlib>
#include <string>

#define likely(x)   __builtin_expect((x), 1)
#define unlikely(x) __builtin_expect((x), 0)

typedef std::string string_t;

typedef unsigned char byte;
