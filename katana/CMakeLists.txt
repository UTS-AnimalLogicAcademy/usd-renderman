set(PLUGIN_NAME usd_renderman_katana)

if(DEFINED ENV{REZ_KATANAUSDPLUGINS_ROOT})
set(USD_KATANA_LIBRARY_DIR $ENV{REZ_KATANAUSDPLUGINS_ROOT}/lib)
set(USD_KATANA_INCLUDE_DIR $ENV{REZ_KATANAUSDPLUGINS_ROOT}/include)
else()
set(USD_KATANA_LIBRARY_DIR ${KATANA_HOME}/plugins/Resources/Usd/lib)
set(USD_KATANA_INCLUDE_DIR ${KATANA_HOME}/plugins/Resources/Usd/include)
endif()

set(RENDERMAN_INCLUDE_DIR $ENV{RMANTREE}/include)
set(RENDERMAN_LIBRARY $ENV{RMANTREE}/lib)

set(PYTHON_VERSION "$ENV{REZ_PYTHON_MAJOR_VERSION}.$ENV{REZ_PYTHON_MINOR_VERSION}")

if(${PYTHON_VERSION} STREQUAL "3.7")
set(PYTHON_LIB_NAME "3.7m")
else()
set(PYTHON_LIB_NAME "${PYTHON_VERSION}")
endif()

set(PYTHON_VERSION_NODOT "$ENV{REZ_PYTHON_MAJOR_VERSION}$ENV{REZ_PYTHON_MINOR_VERSION}")

set(Python_ROOT_DIR "$ENV{REZ_PYTHON_ROOT}/miniconda3")

#set(Python_INCLUDE_DIR "$ENV{REZ_PYTHON_ROOT}/miniconda3/include")
#set(Python_LIBRARY "$ENV{REZ_PYTHON_ROOT}/miniconda3/lib")

set(USD_LIBRARY_DIR ${KATANA_HOME}/bin)
set(USD_INCLUDE_DIR ${KATANA_HOME}/external/FnUSD/include)

if($ENV{REZ_KATANA_MAJOR_VERSION} GREATER 3)
set(PXR_LIB_PREFIX libfn)
else()
set(PXR_LIB_PREFIX libFn)
endif()
find_package(USD REQUIRED)

set(GEOLIB_API_SOURCE_DIR ${KATANA_API_SOURCE_DIR})
message(STATUS "KATANA_API_SOURCE_DIR is ${KATANA_API_SOURCE_DIR}")
message(STATUS "GEOLIB_API_SOURCE_DIR is ${GEOLIB_API_SOURCE_DIR}")

find_package(Renderman REQUIRED)

set(BOOST_LIBRARY_DIR $ENV{BOOST_ROOT}/lib)
set(BOOST_INCLUDE_DIR $ENV{BOOST_ROOT}/include)
set(BOOST_LIBRARYDIR $ENV{BOOST_ROOT}/lib)
set(BOOST_INCLUDEDIR $ENV{BOOST_ROOT}/include)

find_package(Boost
        COMPONENTS
        filesystem
        serialization
        python${PYTHON_VERSION_NODOT}
        system
        thread
        REQUIRED
        )

set(TBB_ROOT_DIR $ENV{TBBROOT})
set(TBB_INCLUDE_DIR $ENV{TBB_INCLUDE_DIR})
set(TBB_LIBRARY $ENV{TBB_LIBRARIES})
find_package(TBB REQUIRED COMPONENTS tbb)
add_definitions(${TBB_DEFINITIONS})

find_package(Python 3.9 COMPONENTS Interpreter Development REQUIRED)


link_directories(
        ${USD_LIBRARY_DIR}
        ${USD_KATANA_LIBRARY_DIR}
        ${KATANA_API_BASE_DIR}/bin
        ${TBB_LIBRARY}
)

include_directories(
        SYSTEM ${KATANA_HOME}/bin/python${PYTHON_VERSION}/include/python${PYTHON_LIB_NAME}
        SYSTEM ${USD_INCLUDE_DIR}
        SYSTEM ${USD_KATANA_INCLUDE_DIR}
        ${TBB_INCLUDE_DIRS}
        SYSTEM ${KATANA_API_INCLUDE_DIR}
        ${CMAKE_SOURCE_DIR}/katana/
        ${Boost_INCLUDE_DIRS}
        SYSTEM ${Python_INCLUDE_DIRS}
)

file(GLOB SRC *.cpp)
add_library(${PLUGIN_NAME} MODULE ${SRC})

target_compile_options(${PLUGIN_NAME} PRIVATE -Wno-deprecated -Wno-unused-parameter -Wall -Wextra)

if(DEFINED ENV{REZ_KATANAUSDPLUGINS_ROOT})
if($ENV{REZ_KATANA_MAJOR_VERSION} GREATER 3)
target_link_libraries(${PLUGIN_NAME}
    CEL
    ${Python_LIBRARIES}
    ${Boost_LIBRARIES}
    ${Boost_PYTHON_LIBRARY}
    ${TBB_LIBRARIES}
    Katana::FnAttribute
    Katana::FnGeolibOpPlugin
    Katana::FnGeolibServices
    fntf
    fngf
    fnsdf
    fnusd
    fnusdGeom
    fnusdVol
    usdKatana
)
else()
target_link_libraries(${PLUGIN_NAME}
    CEL
    ${Python_LIBRARIES}
    ${Boost_LIBRARIES}
    ${Boost_PYTHON_LIBRARY}
    ${TBB_LIBRARIES}
    Katana::FnAttribute
    Katana::FnGeolibOpPlugin
    Katana::FnGeolibServices
    Fntf
    Fngf
    Fnsdf
    Fnusd
    FnusdGeom
    FnusdVol
    usdKatana
)
endif()
else()
if($ENV{REZ_KATANA_MAJOR_VERSION} GREATER 3)
target_link_libraries(${PLUGIN_NAME}
    CEL
    ${Python_LIBRARIES}
    ${Boost_LIBRARIES}
    ${Boost_PYTHON_LIBRARY}
    ${TBB_LIBRARIES}
    Katana::FnAttribute
    Katana::FnGeolibOpPlugin
    Katana::FnGeolibServices
    fntf
    fngf
    fnsdf
    fnusd
    fnusdGeom
    fnusdVol
    ${USD_KATANA_LIBRARY_DIR}/FnusdKatana.so
)
else()
target_link_libraries(${PLUGIN_NAME}
    CEL
    ${Python_LIBRARIES}
    ${Boost_LIBRARIES}
    ${Boost_PYTHON_LIBRARY}
    ${TBB_LIBRARIES}
    Katana::FnAttribute
    Katana::FnGeolibOpPlugin
    Katana::FnGeolibServices
    Fntf
    Fngf
    Fnsdf
    Fnusd
    FnusdGeom
    FnusdVol
    ${USD_KATANA_LIBRARY_DIR}/FnusdKatana.so
)
endif()
endif()

set_target_properties(${PLUGIN_NAME} PROPERTIES PREFIX "")
set_target_properties(${PLUGIN_NAME} PROPERTIES INSTALL_RPATH_USE_LINK_PATH ON)

install(TARGETS ${PLUGIN_NAME} DESTINATION Resources/Ops)
