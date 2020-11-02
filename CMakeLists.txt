cmake_minimum_required(VERSION 3.2)

set (CMAKE_CXX_STANDARD 11)

set(CMAKE_MODULE_PATH
        "${KATANA_HOME}/plugins/Src/cmake"        
)

set(CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake/defaults
                      ${CMAKE_SOURCE_DIR}/cmake/modules
                      ${CMAKE_SOURCE_DIR}/cmake/macros)

# boost
set(BOOST_ROOT "$ENV{REZ_BOOST_ROOT}")

# tbb
set(TBB_ROOT_DIR "$ENV{REZ_TBB_ROOT}")
set(TBB_INCLUDE_DIR "$ENV{REZ_TBB_ROOT}/include")
set(TBB_LIBRARY "$ENV{REZ_TBB_ROOT}/lib/intel64/gcc4.4/")
set(TBB_LIBRARY "$ENV{TBB_LIBRARIES}")


include(Options)
include(ProjectDefaults)
include(Packages)

set(KATANA_HOME "$ENV{KATANA_HOME}" CACHE PATH "Path to Katana")

find_package(Katana PATHS "${KATANA_HOME}/plugin_apis/cmake" REQUIRED)
add_compile_options(-Wall)

#add_definitions(-DBOOST_ERROR_CODE_HEADER_ONLY)

# Ensure we don't compile DSOs with undefined symbols.
set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} -Wl,--no-undefined")
set(CMAKE_MODULE_LINKER_FLAGS "${CMAKE_MODULE_LINKER_FLAGS} -Wl,--no-undefined")

set(USD_LIBRARY_DIR $ENV{REZ_USD_ROOT}/lib)
set(USD_INCLUDE_DIR $ENV{REZ_USD_ROOT}/include)

find_package(USD REQUIRED)
find_package(PythonLibs REQUIRED)

include_directories(SYSTEM ${USD_INCLUDE_DIR})
link_directories(${USD_LIBRARY_DIR})

include_directories(SYSTEM ${TBB_INCLUDE_DIRS})
include_directories(SYSTEM ${PYTHON_INCLUDE_DIRS})

add_subdirectory(katana)
