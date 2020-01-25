#pragma once

#include <exception>
#include <string>

class ParameterException : public std::exception
{

public:

  ParameterException(std::string msg, std::string param) noexcept :
    m_msg((msg + " " + param).c_str())
  {
  }

  const char* what() const noexcept
  {
    return m_msg;
  }

private:
  
  const char* m_msg;

};