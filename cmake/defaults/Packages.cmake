#
# Copyright 2016 Pixar
#
# Licensed under the Apache License, Version 2.0 (the "Apache License")
# with the following modification; you may not use this file except in
# compliance with the Apache License and the following modification to it:
# Section 6. Trademarks. is deleted and replaced with:
#
# 6. Trademarks. This License does not grant permission to use the trade
#    names, trademarks, service marks, or product names of the Licensor
#    and its affiliates, except as required to comply with Section 4(c) of
#    the License and to reproduce the content of the NOTICE file.
#
# You may obtain a copy of the Apache License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the Apache License with the above modification is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the Apache License for the specific
# language governing permissions and limitations under the Apache License.
#

# Save the current value of BUILD_SHARED_LIBS and restore it at
# the end of this file, since some of the Find* modules invoked
# below may wind up stomping over this value.
set(build_shared_libs "${BUILD_SHARED_LIBS}")

# USD Renderman Requirements
# ----------------------------------------------

set(USD_LIBRARY_DIR $ENV{REZ_USD_ROOT}/lib)
set(USD_INCLUDE_DIR $ENV{REZ_USD_ROOT}/include)

find_package(USD REQUIRED)

# USD Renderman HD Renderer Requirement
# ----------------------------------------------
if (BUILD_USD_PLUGIN OR BUILD_USD_IMAGING_PLUGIN)
    find_package(GLEW REQUIRED)
endif ()

# Core USD Package Requirements 
# ----------------------------------------------

# Threads.  Save the libraries needed in PXR_THREAD_LIBS;  we may modify
# them later.  We need the threads package because some platforms require
# it when using C++ functions from #include <thread>.
set(CMAKE_THREAD_PREFER_PTHREAD TRUE)
find_package(Threads REQUIRED)
set(PXR_THREAD_LIBS "${CMAKE_THREAD_LIBS_INIT}")

if(PXR_ENABLE_PYTHON_SUPPORT)
    # --Python.  We are generally but not completely 2.6 compliant.
    # We don't need this flag if we are on 0.8.2.
    if (${USD_VERSION} VERSION_LESS "0.8.2")
        add_definitions(-DPXR_PYTHON_SUPPORT_ENABLED)
    endif ()
    find_package(PythonInterp 2.7 REQUIRED)
    find_package(PythonLibs 2.7 REQUIRED)

    # --Boost
    set(Boost_USE_STATIC_LIBS OFF)
    find_package(Boost
        COMPONENTS
            python
        REQUIRED
    )

else()
    find_package(PythonInterp 2.7 REQUIRED)
endif()

# --TBB

find_package(TBB REQUIRED COMPONENTS tbb)
add_definitions(${TBB_DEFINITIONS})


if (NOT PXR_MALLOC_LIBRARY)
    if (NOT WIN32)
        message(STATUS "Using default system allocator because PXR_MALLOC_LIBRARY is unspecified")
    endif()
endif()


# Third Party Plugin Package Requirements
# ----------------------------------------------


# ----------------------------------------------

set(BUILD_SHARED_LIBS "${build_shared_libs}")
