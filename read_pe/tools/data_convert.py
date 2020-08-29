def b_to_int(data: bytes):
    data_len = len(data)
    assert data_len > 0 and data_len <= 8
    return int.from_bytes(data, byteorder="little")


def b_to_hex(data: bytes):
    return " ".join('0x{:02x}'.format(x) for x in data)

def b_to_ascii(data: bytes):
    return data.decode('ascii')