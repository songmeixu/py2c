import cppyy
cppyy.include('zlib.h')
cppyy.load_library('libz')
ver = cppyy.gbl.zlibVersion()

print(ver)
