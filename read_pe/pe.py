# from .elf_header import ElfHeader
# from .sections import Sections
from .dos_header import DosHeader

# the entier elf
class PE:
    def __init__(self, path):
        super().__init__()
        self.content = open(path, 'rb').read()
        self.len = len(self.content)
        self.dos_header = DosHeader(self)
        # self.elf_header = ElfHeader(self)
        # self.sections = Sections(self, self.elf_header.shoff, self.elf_header.shnum, self.elf_header.shentsize)

    def get_sh_by_name(self, name):
        l = [s for s in self.sections.shs if s.name == name]
        return next(iter(l), None)

    def extra(self, index: int, size: int) -> int:
        return self.content[index: index + size]

    def is_64(self):
        return self.elf_header.is_64()

    def part(self, start, size, start_64 = -1, size_64 = -1):
        return self.elf_header.part(start, size, start_64, size_64)

    def pp_strs_content(self):
        str_content = self.sections.str_section_content()
        for i in range(0, len(str_content)):
            print(f"Section {i}:")
            content_bytes = str_content[i]
            print(", ".join([s.decode('utf-8') for s in content_bytes.split(b'\x00')]))

    def pp(self):
        print("Dos Header:\n" + self.dos_header.pp_str())
