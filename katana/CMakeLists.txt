set(PLUGIN_NAME usd_renderman_katana)

set(USD_KATANA_INCLUDE_DIR $ENV{REZ_USD_KATANA_ROOT}/third_party/katana/include)
set(USD_KATANA_LIBRARY_DIR $ENV{REZ_USD_KATANA_ROOT}/third_party/katana/lib)

set(RENDERMAN_INCLUDE_DIR $ENV{RMANTREE}/include)
set(RENDERMAN_LIBRARY $ENV{RMANTREE}/lib)

find_package(Renderman REQUIRED)
find_package(Katana REQUIRED)

find_package(Boost
        COMPONENTS
        filesystem
        serialization
        python
        system
        REQUIRED
)

link_directories(${USD_KATANA_LIBRARY_DIR})

file(GLOB FNATTRIBUTE_SRC ${KATANA_API_SOURCE_DIR}/FnAttribute/client/*.cpp)
file(GLOB FNGEOLIBOP_SRC ${KATANA_API_SOURCE_DIR}/FnGeolib/op/*.cpp)
file(GLOB FNGEOLIBUTIL_SRC ${KATANA_API_SOURCE_DIR}/FnGeolib/util/*.cpp)
file(GLOB FNGEOLIBSERVICES_SRC ${KATANA_API_SOURCE_DIR}/FnGeolibServices/client/*.cpp)
file(GLOB FNPLUGINMANAGER_SRC ${KATANA_API_SOURCE_DIR}/FnPluginManager/client/*.cpp)
file(GLOB FNPLUGINSYSTEM_SRC ${KATANA_API_SOURCE_DIR}/FnPluginSystem/*.cpp)
file(GLOB FNLOGGING_SRC ${KATANA_API_SOURCE_DIR}/FnLogging/client/*.cpp)
file(GLOB PYSTRING_SRC ${KATANA_API_SOURCE_DIR}/pystring/*.cpp)

link_directories(${KATANA_API_BASE_DIR}/bin)

include_directories(        
        ${CMAKE_SOURCE_DIR}/katana/
        ${Boost_INCLUDE_DIRS}
)

file(GLOB SRC *.cpp)
set(API_SRC
    ${FNATTRIBUTE_SRC}
    ${FNGEOLIBOP_SRC}
    ${FNGEOLIBUTIL_SRC}
    ${FNGEOLIBSERVICES_SRC}
    ${FNPLUGINMANAGER_SRC}
    ${FNPLUGINSYSTEM_SRC}
    ${FNLOGGING_SRC}
    ${PYSTRING_SRC}
)

add_library(${PLUGIN_NAME} MODULE ${SRC} ${API_SRC})

set_target_properties(${PLUGIN_NAME} PROPERTIES PREFIX "")
set_target_properties(${PLUGIN_NAME} PROPERTIES INSTALL_RPATH_USE_LINK_PATH ON)

target_include_directories(${PLUGIN_NAME} SYSTEM PRIVATE ${Boost_INCLUDE_DIRS})
target_include_directories(${PLUGIN_NAME} PRIVATE ${KATANA_API_INCLUDE_DIR})
target_include_directories(${PLUGIN_NAME} PRIVATE ${USD_KATANA_INCLUDE_DIR})
target_include_directories(${PLUGIN_NAME} PRIVATE ${USD_INCLUDE_DIR})
target_include_directories(${PLUGIN_NAME} PRIVATE ${RENDERMAN_INCLUDE_DIR})

link_directories(
        $ENV{REZ_USD_ROOT}/lib
        $ENV{REZ_TBB_ROOT}/lib/intel64/gcc4.4/
)

include_directories(
        $ENV{REZ_USD_ROOT}/include
)

target_link_libraries(${PLUGIN_NAME}
    CEL
    ${PYTHON_LIBRARIES}
    ${Boost_LIBRARIES}
    ${Boost_PYTHON_LIBRARY}
    Katana::FnAttribute
    Katana::FnGeolibOpPlugin
    Katana::FnGeolibServices
    dl
    tf
    gf
    sdf
    usd
    usdGeom
    usdVol
    usdKatana
    ${USD_KATANA_LIBRARY_DIR}
    ${USD_LIBRARY_DIR}
    $ENV{PRMAN_LIBS}
    ${RENDERMAN_LIBRARY}
)

install(TARGETS ${PLUGIN_NAME} DESTINATION Resources/Ops)
