cmake_minimum_required(VERSION 3.10)

project(WarcraftLogs)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

function(ADD_PROJECT_LIBRARY LIBRARY_NAME)
    set(LIB_FILES)
    file(GLOB LIB_FILES ${SOURCE_WILDCARDS})
    if(LIB_FILES)
        add_library(${LIBRARY_NAME} ${LIB_FILES})
        set(ENV{LIBRARY_NAMES} "$ENV{LIBRARY_NAMES};${LIBRARY_NAME}")
    endif(LIB_FILES)
endfunction(ADD_PROJECT_LIBRARY)

set(SOURCE_WILDCARDS *.cpp)
set(ENV{LIBRARY_NAMES})

add_subdirectory(wlog2cpp)

# add_executable(WarcraftLogs source/main.cpp ${SRC_FILES})
