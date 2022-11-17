# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles/startGui_autogen.dir/AutogenUsed.txt"
  "CMakeFiles/startGui_autogen.dir/ParseCache.txt"
  "startGui_autogen"
  )
endif()
