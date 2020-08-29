class SectionType():
    def __init__(self, value, name, meaning):
        super().__init__()
        self.value = value
        self.name = name
        self.meaning = meaning

s_null = SectionType(0x0, "SHT_NULL", "Section header table entry unused")
s_progbits = SectionType(0x1, "SHT_PROGBITS", "Program data")
s_symtab = SectionType(0x2, "SHT_SYMTAB", "Symbol table")
s_strtab = SectionType(0x3, "SHT_STRTAB", "String table")
s_rela = SectionType(0x4, "SHT_RELA", "Relocation entries with addends")
s_hash = SectionType(0x5, "SHT_HASH", "Symbol hash table")
s_dynamic = SectionType(0x6, "SHT_DYNAMIC", "Dynamic linking information")
s_note = SectionType(0x7, "SHT_NOTE", "Notes")
s_nobits = SectionType(0x8, "SHT_NOBITS", "Program space with no data (bss)")
s_rel = SectionType(0x9, "SHT_REL", "Relocation entries, no addends")
s_shlib = SectionType(0xa, "SHT_SHLIB", "Reserved")
s_dynsym = SectionType(0xb, "SHT_DYNSYM", "Dynamic linker symbol table")
s_init_array = SectionType(0xe, "SHT_INIT_ARRAY", "Array of constructors")
s_fini_array = SectionType(0xf, "SHT_FINI_ARRAY", "Array of destructors")
s_preinit_array = SectionType(0x10, "SHT_PREINIT_ARRAY", "Array of pre-constructors")
s_group = SectionType(0x11, "SHT_GROUP", "Section group")
s_symtab_shndx = SectionType(0x12, "SHT_SYMTAB_SHNDX", "Extended section indices")
s_num = SectionType(0x13, "SHT_NUM", "Number of defined types.")
s_loos = SectionType(0x60000000, "SHT_LOOS", "Start OS-specific.")