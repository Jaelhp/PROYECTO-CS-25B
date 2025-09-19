# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\ProyectoFerreteria_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\ProyectoFerreteria_autogen.dir\\ParseCache.txt"
  "ProyectoFerreteria_autogen"
  )
endif()
