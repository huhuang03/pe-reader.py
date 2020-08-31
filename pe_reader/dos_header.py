from .tools.data_convert import *

class DosHeader():
    def __init__(self, pe):
        super().__init__()
        self.pe = pe
        self.e_magic = self.part(0, 2)
        self.e_cblp = self.part(2, 4)
        self.e_cp = self.part(0, 2)
        self.e_crlc = self.part(0, 2)
        self.e_cparhdr = self.part(0, 2)
        self.e_minalloc = self.part(0, 2)
        self.e_maxalloc = self.part(0, 2)
        self.e_ss = self.part(0, 2)
        self.e_sp = self.part(0, 2)
        self.e_csum = self.part(0, 2)
        self.e_ip = self.part(0, 2)
        self.e_cs = self.part(0, 2)
        self.e_lfarlc = self.part(0, 2)
        self.e_ovno = self.part(0, 2)
        self.e_res[4] = self.part(0, 2)
        self.e_oemid = self.part(0, 2)
        self.e_oeminfo = self.part(0, 2)
        self.e_res2[10] = self.part(0, 2)
        self.e_lfanew = self.part(0, 2)

        assert b_to_ascii(self.e_magic) == 'MZ', "Why magic is not MZ, and the magic is: " + b_to_hex(self.e_magic)

    def is_32(self):
        return True

    def is_64(self):
        return False

    def part(self, start, size, start_64 = -1, size_64 = -1):
        if start_64 < 0:
            start_64 = start
        if size_64 < 0:
            size_64 = size

        if self.is_64():
            start = start_64
            size = size_64
        return self.pe.extra(start, size)

    def pp_str(self):
        return "Magic:\t" + b_to_ascii(self.e_magic) + "(" + b_to_hex(self.e_magic) + ")"