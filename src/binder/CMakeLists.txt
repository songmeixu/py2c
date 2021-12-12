#
# Set up the Cppyy bindings generation. This is a customized version defined
# in boink's cmake/ dir; it uses genreflex rather than calling rootcling directly.
# I did this because I couldn't get rootcling to properly include/exclude classes
# via the LinkDef header, and I wanted to be able to use the better syntax in
# the genreflex selection XML anyhow. Also, I think this is now the recommended /
# more modern way anyhow? Code was modified from the versions cppyy distributes.
#

# get glog/logging.h path
get_target_property(glog_INCLUDE_PATH glog INCLUDE_DIRECTORIES)
foreach (inc_path ${glog_INCLUDE_PATH})
  if (${inc_path} MATCHES "\\$<BUILD_INTERFACE:(.*)>.*")
     list(APPEND glog_INCLUDE_DIRS ${CMAKE_MATCH_1})
  endif ()
endforeach ()

cppyy_add_bindings(
    k2 "${PROJECT_VERSION}" "Meixu Song" "songmeixu@outlook.com"
    LICENSE "MIT"
    LANGUAGE_STANDARD "14"
    SELECTION_XML ${CMAKE_CURRENT_LIST_DIR}/selection.xml
    INTERFACE_FILE ${public_header_file}
    HEADERS ${ABS_HEADERS_TO_BINDER}
    INCLUDE_DIRS ${CMAKE_SOURCE_DIR}/${CMAKE_PROJECT_NAME}/cc
                 ${PYBIND11_INCLUDE_DIR}
                 ${PYTHON_INCLUDE_DIRS}
                 ${glog_INCLUDE_DIRS}
    LINK_LIBRARIES k2
    NAMESPACES kk
)

install(TARGETS k2
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/${CMAKE_PROJECT_NAME}
        )

install(CODE "execute_process(COMMAND pip install ${PY_WHEEL_FILE})")
