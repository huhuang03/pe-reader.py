// https://en.wikipedia.org/wiki/Executable_and_Linkable_Format#:~:text=In%20computing%2C%20the%20Executable%20and,shared%20libraries%2C%20and%20core%20dumps.&text=By%20design%2C%20the%20ELF%20format,extensible%2C%20and%20cross%2Dplatform.

// this script extra the machine from wiki.
table = document.getElementsByClassName("wikitable")[3]
tbody = table.firstElementChild
tars = tbody.children

function extra_start_and_end(value) {
    let reg = /(.*)-(.*)/
    match = value.match(reg)
    start = parseInt(match[1].trim(), 16)
    end = parseInt(match[2].trim(), 16)
    return [start, end]
}

extra_test = extra_start_and_end("0x100 - 0x200")
console.assert(extra_test[0] == 0x100)
console.assert(extra_test[1] == 0x200)

function to_hex_str(val) {
    return ("00" + val.toString(16)).slice(-2)
}

rst = ""
var index = 0
for (var i = 0; i < tars.length; i++) {
    tr = tars[i];
    value = tr.children[0].textContent.trim()
    isa = tr.children[1].textContent.trim()
    if (value.startsWith("0x")) {
        start = 0
        end = 0
        if (value.includes('-')) {
            extra_test = extra_start_and_end(value)
            start = extra_test[0]
            end = extra_test[1]
        } else {
            start = parseInt(value, 16)
            end = start
        }

        while (start <= end) {
            rst += `machine_${index} = Machine(0x${to_hex_str(start)}, "${isa}")`
            rst += "\n"
            index++;
            start += 1
        }
    }
}
console.log(rst);