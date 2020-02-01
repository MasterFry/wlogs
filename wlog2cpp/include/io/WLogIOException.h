#pragma once

#include <exception>
#include <string>

class WLogIOException : public std::exception
{

protected:

  std::string message;

public:

  WLogIOException(std::string message) noexcept :
    message(message)
  {
  }

  const char* what() const noexcept
  {
    return message.c_str();
  }

};