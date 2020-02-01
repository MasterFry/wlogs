#pragma once

#include <cstdio>

class IWriteable
{

public:

  virtual void write(FILE* file) = 0;

};
