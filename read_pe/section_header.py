from tools.data_convert import *

class SectionHeader:
    def __init__(self, elf, start):
        super().__init__()
        self.elf = elf
        self.start = start

        self.sh_name = self.elf.part(start + 0, 4)
        self.i_name = b_to_int(self.sh_name)
        self.name = "unk"

        self.sh_type = self.elf.part(start + 4, 4)
        self.sh_flags = self.elf.part(start + 8, 4, start + 8, 8)
        self.sh_addr = self.elf.part(start + 0xc, 4, start + 0x10, 8)
        self.sh_offset = self.elf.part(start + 0x10, 4, start + 0x18, 8)
        self.sh_size = self.elf.part(start + 0x14, 4, start + 0x20, 8)
        self.sh_link = self.elf.part(start + 0x18, 4, start + 0x28)
        self.sh_info = self.elf.part(start + 0x1c, 4, start + 0x2c)
        self.sh_addralign = self.elf.part(start + 0x20, 4, start + 0x20, 8)
        self.sh_entsize = self.elf.part(start + 0x24, 4, start + 0x38, 8)

        self.type = b_to_int(self.sh_type)
        self.size = b_to_int(self.sh_size)
        self.offset = b_to_int(self.sh_offset)

        def pp():
            return f"sh_offset: "

    def __str__(self):
        return f"Section(offset = {hex(self.offset)}, size={self.size})"