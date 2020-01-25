#pragma once

#include <exception>
#include <fstream>

class WLogFileException : public std::exception
{

public:

  WLogFileException(const char* msg, std::streampos pos) noexcept :
    m_msg(msg),
    m_pos(pos)
  {
  }

  const char* what() const noexcept
  {
    return m_msg;
  }

  std::streampos getPos() const noexcept
  {
    return m_pos;
  }

private:
  
  const char* m_msg;
  std::streampos m_pos;

};