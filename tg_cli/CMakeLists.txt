get_directory_property(HAS_PARENT PARENT_DIRECTORY)
if (HAS_PARENT)
  set(TL_TD_AUTO_INCLUDES ${TL_TD_AUTO_INCLUDES} PARENT_SCOPE)
  set(TL_TD_API_TLO ${TL_TD_API_TLO} PARENT_SCOPE)
  set(TL_TD_JSON_AUTO ${TL_TD_JSON_AUTO} PARENT_SCOPE)
  set(TD_TEST_SOURCE ${TD_TEST_SOURCE} PARENT_SCOPE)
endif()


#SOURCE SETS

set_source_files_properties(${TL_TD_AUTO} PROPERTIES GENERATED TRUE)
if (TD_API_JAVA_PACKAGE)
  set(TL_JNI_OBJECT
    td/tl/tl_jni_object.cpp
    td/tl/tl_jni_object.h
  )
else()
  set(TL_JNI_OBJECT)
endif()

set(TL_TD_SCHEME_SOURCE
  ${TL_TD_AUTO}
  ${TL_JNI_OBJECT}
  td/tl/TlObject.h
  td/tl/tl_object_parse.h
  td/tl/tl_object_store.h
)

set_source_files_properties(${TL_TD_JSON_AUTO} PROPERTIES GENERATED TRUE)
set(TL_TD_JSON
  ${TL_TD_JSON_AUTO}
  td/tl/tl_json.h
)

set_source_files_properties(${TL_C_AUTO} PROPERTIES GENERATED TRUE)
set(TL_C_SCHEME_SOURCE
  ${TL_C_AUTO}
)
#EXECUTABLES
if (NOT CMAKE_CROSSCOMPILING)
  add_executable(tg_cli td/telegram/cli.cpp ${TL_TD_JSON})
    set(CMAKE_EXE_LINKER_FLAGS " -static")
  target_link_libraries(tg_cli PRIVATE memprof tdcore tdtl -static-libgcc -static-libstdc++)
  add_dependencies(tg_cli tl_generate_json)
endif()
