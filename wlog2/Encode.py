
def encodeInt(value: int, size: int) -> bytes:
    return value.to_bytes(length=size, byteorder='little')
