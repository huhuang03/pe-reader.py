_B_SPLIT = b'\x00'

class SectionStr():
    def __init__(self, elf, header):
        super().__init__()
        self.elf = elf
        self.h = header
        self.content = self.elf.content[self.h.offset: self.h.offset + self.h.size]

        self.strs = [b.decode('utf-8') for b in self.content.split(_B_SPLIT)]

        if self.strs[0] == '' and self.strs[-1] == '':
            self.strs = self.strs[1: -1]

    def get_str(self, index):
        """
        param index: the index of bytes.
        """
        print(index)
        print(self.content)
        print(self.content[index: index + 1])
        end = self.content.index(_B_SPLIT, index + 1)

        # handle first str, which is starts with _B_SPLIT
        start = index
        if index == 0 and self.content[index] == _B_SPLIT:
            start = 1
        content = self.content[start: end]
        print(content)

        return content.decode('utf-8')


    def pp_str(self):
        return ", ".join(self.strs)

