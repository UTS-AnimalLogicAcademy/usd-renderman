cmake_minimum_required(VERSION 3.2)

set (CMAKE_CXX_STANDARD 11)

project(usd-renderman)

set(KATANA_HOME "$ENV{KATANA_HOME}" CACHE PATH "Path to Katana")

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH}
                      ${CMAKE_CURRENT_SOURCE_DIR}/cmake/modules
                      "${KATANA_HOME}/plugins/Src/cmake"
)

find_package(Katana PATHS "${KATANA_HOME}/plugin_apis/cmake" REQUIRED)

# Ensure we don't compile DSOs with undefined symbols.
set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} -Wl,--no-undefined")
set(CMAKE_MODULE_LINKER_FLAGS "${CMAKE_MODULE_LINKER_FLAGS} -Wl,--no-undefined")

add_subdirectory(katana)
