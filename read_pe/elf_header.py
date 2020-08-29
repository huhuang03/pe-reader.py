from base_elf_part import BaseELFPart
from tools.data_convert import *

_INDEX_CLASS = 0x4
_INDEX_MACHINE = 0x12

CLAZZ_32 = 1
CLAZZ_64 = 2

class ElfHeader(BaseELFPart):
    def __init__(self, elf):
        super().__init__(elf)
        self.clazz = CLAZZ_32
        self.e_class = self.part(_INDEX_CLASS, 1)
        self.clazz = b_to_int(self.e_class)
        assert self.is_32() or self.is_64()

        self.e_shoff = self.part(0x20, 4, 0x28, 8)
        self.shoff = b_to_int(self.e_shoff)

        self.e_shnum = self.part(0x30, 1, 0x3c)
        self.shnum = b_to_int(self.e_shnum)

        self.e_shentsize = self.part(0x2E, 2, 0x3A)
        self.shentsize = b_to_int(self.e_shentsize)
        self._check_section_end_file()

        self.e_entry = self.part(0x18, 4, 0x18, 8)
        self.entry = b_to_int(self.e_entry)

        self.e_shstrndx = self.part(0x32, 2, 0x3e)
        self.shstrndx = b_to_int(self.e_shstrndx)

        self._machine = self.part(_INDEX_MACHINE, 2)
        # _machine has size 2 but only 1 byte useful
        assert(self._machine[1] == 0x00)
        self._machine = self._machine[:1]

    def pp(self):
        return f"e_machine: {b_to_hex(self._machine)}"\
            + f"\nentry: {hex(self.entry)}"\
            + f"\nsecton: offset: {hex(self.shoff)}, shnum: {self.shnum}, shentsize: {self.shentsize}, shstrndx: {self.shstrndx}"

    def _check_section_end_file(self):
        section_end = self.shoff + self.shentsize * self.shnum
        assert section_end == self.elf.len

    def is_32(self):
        return CLAZZ_32 == self.clazz

    def is_64(self):
        return CLAZZ_64 == self.clazz

    def part(self, start, size, start_64 = -1, size_64 = -1):
        if start_64 < 0:
            start_64 = start
        if size_64 < 0:
            size_64 = size

        if self.is_64():
            start = start_64
            size = size_64
        return self.elf.extra(start, size)
