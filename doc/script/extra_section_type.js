// https://en.wikipedia.org/wiki/Executable_and_Linkable_Format#:~:text=In%20computing%2C%20the%20Executable%20and,shared%20libraries%2C%20and%20core%20dumps.&text=By%20design%2C%20the%20ELF%20format,extensible%2C%20and%20cross%2Dplatform.

// this script extra the machine from wiki.
table = document.getElementsByClassName("wikitable")[7]
tbody = table.firstElementChild
tars = tbody.children

function to_hex_str(val) {
    return val.toString(16)
}

rst = ""
var index = 0
for (var i = 0; i < tars.length; i++) {
    tr = tars[i];
    value = tr.children[0].textContent.trim()
    name = tr.children[1].textContent.trim()
    meaning = tr.children[2].textContent.trim()
    if (value.startsWith("0x")) {
        start = 0
        end = 0
        start = parseInt(value, 16)
        end = start

        while (start <= end) {
            rst += `s_${name.slice(4).toLowerCase()} = SectionType(0x${to_hex_str(start)}, "${name}", "${meaning}")`
            rst += "\n"
            index++;
            start += 1
        }
    }
}
console.log(rst);