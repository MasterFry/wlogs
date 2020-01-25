cmake_minimum_required(VERSION 3.10)

project(BuffGenerator)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

file(GLOB src *.cpp)
include_directories(BuffGenerator PUBLIC "${PROJECT_SOURCE_DIR}")

add_executable(BuffGenerator main.cpp ${src})
