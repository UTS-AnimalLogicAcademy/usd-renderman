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


if(DEFINED ENV{CXX11_ABI_IGNORE})
        set(CMAKE_CXX_FLAGS "${_PXR_CXX_FLAGS} -D_GLIBCXX_USE_CXX11_ABI=0 ${CMAKE_CXX_FLAGS}")
        message(INFO " CXX11_ABI_IGNORE set. Ignoring CXX11 flags.")
else()
        set(CMAKE_CXX_FLAGS "${_PXR_CXX_FLAGS} ${CMAKE_CXX_FLAGS}")
endif(DEFINED ENV{CXX11_ABI_IGNORE})

add_subdirectory(katana)
