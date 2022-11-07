set(PLUGIN_NAME usd_renderman_katana)

set(USD_KATANA_LIBRARY_DIR $ENV{REZ_KATANAUSDPLUGINS_ROOT}/lib)
set(USD_KATANA_INCLUDE_DIR $ENV{REZ_KATANAUSDPLUGINS_ROOT}/include)

set(RENDERMAN_INCLUDE_DIR $ENV{RMANTREE}/include)
set(RENDERMAN_LIBRARY $ENV{RMANTREE}/lib)

set(USD_LIBRARY_DIR /opt/Foundry/Katana3.6v2/bin)
set(USD_INCLUDE_DIR /opt/Foundry/Katana3.6v2/external/FnUSD/include)
set(PXR_LIB_PREFIX libFn)
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
        python27
        system
        thread
        REQUIRED
        )

set(TBB_ROOT_DIR $ENV{TBBROOT})
set(TBB_INCLUDE_DIR $ENV{TBB_INCLUDE_DIR})
set(TBB_LIBRARY $ENV{TBB_LIBRARIES})
find_package(TBB REQUIRED COMPONENTS tbb)
add_definitions(${TBB_DEFINITIONS})

find_package(PythonLibs REQUIRED)


link_directories(
        ${USD_LIBRARY_DIR}
        ${USD_KATANA_LIBRARY_DIR}
        ${KATANA_API_BASE_DIR}/bin
        ${TBB_LIBRARY}
)

include_directories(
        SYSTEM /opt/Foundry/Katana3.6v2/./bin/python2.7/include/python2.7
        SYSTEM ${USD_INCLUDE_DIR}
        SYSTEM ${USD_KATANA_INCLUDE_DIR}
        ${TBB_INCLUDE_DIRS}
        SYSTEM ${KATANA_API_INCLUDE_DIR}
        ${CMAKE_SOURCE_DIR}/katana/
        ${Boost_INCLUDE_DIRS}
        SYSTEM ${PYTHON_INCLUDE_DIRS}
)

file(GLOB SRC *.cpp)
add_library(${PLUGIN_NAME} MODULE ${SRC})

target_compile_options(${PLUGIN_NAME} PRIVATE -Wno-deprecated -Wno-unused-parameter -Wall -Wextra)

target_link_libraries(${PLUGIN_NAME}
    CEL
    ${PYTHON_LIBRARIES}
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

set_target_properties(${PLUGIN_NAME} PROPERTIES PREFIX "")
set_target_properties(${PLUGIN_NAME} PROPERTIES INSTALL_RPATH_USE_LINK_PATH ON)

install(TARGETS ${PLUGIN_NAME} DESTINATION Resources/Ops)
