from section_header import SectionHeader
import section_type
from section_str import SectionStr

class Sections():
    def __init__(self, elf, shoff, shnum, shentsize):
        super().__init__()
        self.elf = elf
        self.shoff = shoff
        self.shnum = shnum
        self.shentsize = shentsize
        self.shs = []
        for i in range(0, shnum):
            start = shoff + i * shentsize
            self.shs.append(SectionHeader(self.elf, start))

        self.sh_shstr = self.shs[self.elf.elf_header.shstrndx]
        assert self.sh_shstr.type == section_type.s_strtab.value

        self.s_str = SectionStr(self.elf, self.sh_shstr)
        for sh in self.shs:
            # print(self.s_str.strs)
            # print(len(self.s_str.strs))
            sh.name = self.s_str.get_str(sh.i_name)

    def str_section_content(self):
        """
        return: list of string bytes.
        """
        return [self.elf.content[s.offset: s.offset + s.size] for s in self.s_strs]
    
    def get_section_by_name(self, name):
        return [s for s in self.shs if s.name == name]

    def pp_str(self):
        rst = "Section: \n\t"\
            + "\n\t".join([sh.name for sh in self.shs])
        return rst