# Fixed: maxsplit=1 keeps any additional "=" characters in the value.
piece = "note=server=east"
key, value = piece.split("=", 1)
print(key, value)
