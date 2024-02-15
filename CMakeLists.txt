cmake_minimum_required(VERSION 3.2)

set (CMAKE_CXX_STANDARD 17)

project(usd-renderman)

set(KATANA_HOME $ENV{KATANA_HOME} CACHE PATH "Path to Katana")

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH}
                      ${CMAKE_CURRENT_SOURCE_DIR}/cmake/modules
                      "${KATANA_HOME}/plugins/Src/cmake"
)

set(KATANA_RESOURCES "$ENV{KATANA_RESOURCES}")

find_package(Katana PATHS "${KATANA_HOME}/plugin_apis/cmake" REQUIRED)

# Ensure we don't compile DSOs with undefined symbols.
set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} -Wl,--no-undefined -pthread")
set(CMAKE_MODULE_LINKER_FLAGS "${CMAKE_MODULE_LINKER_FLAGS} -Wl,--no-undefined -pthread")

add_subdirectory(katana)
