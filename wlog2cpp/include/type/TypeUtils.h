#pragma once

#include "std.h"

#define AURA_TYPE_NAMES_COUNT           2
#define ENVIRONMENTAIL_TYPE_NAMES_COUNT 6
#define EVENT_TYPE_NAMES_COUNT          50
#define GUID_TYPE_NAMES_COUNT           9
#define MISS_TYPE_NAMES_COUNT           10

namespace types
{

  int findNameInArray(string_t name, const char* array[], size_t length);

};
