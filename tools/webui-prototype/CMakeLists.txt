cmake_minimum_required(VERSION 3.16)
project(WebUIPrototype LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 COMPONENTS Widgets WebEngineWidgets WebChannel REQUIRED)

set(SOURCES
  main.cpp
  WebHost.cpp
)

add_executable(WebUIPrototype ${SOURCES} resources.qrc)

target_include_directories(WebUIPrototype PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})
target_link_libraries(WebUIPrototype PRIVATE Qt6::Widgets Qt6::WebEngineWidgets Qt6::WebChannel)
