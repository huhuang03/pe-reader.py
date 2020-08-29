from .tools.data_convert import *

class DosHeader():
    def __init__(self, pe):
        super().__init__()
        self.pe = pe
        self.b_magic = self.part(0, 2)
        assert b_to_ascii(self.b_magic) == 'MZ', "Why magic is not MZ, and the magic is: " + b_to_hex(self.b_magic)

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
        return "Magic:\t" + b_to_ascii(self.b_magic) + "(" + b_to_hex(self.b_magic) + ")"