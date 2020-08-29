# import os
# from elf import ELF

# if os.name == "posix":
#     ELF_PATH = "/Users/th/source/dy_re/libcms_crack/libcms.so"
# else:
#     ELF_PATH = "D:\\s\\dy_re\\cms_crack\\libcms.so"


# ELF(ELF_PATH).pp()
from read_pe import PE
DLL_PATH = "D:\\s\\test\\python\\c_sample\\build\\Debug\\sample.dll"

PE(DLL_PATH).pp()