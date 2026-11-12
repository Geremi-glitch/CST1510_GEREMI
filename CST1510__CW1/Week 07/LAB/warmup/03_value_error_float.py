# Fixed: catch invalid numeric text so one bad value does not crash the program.
raw_line = "srv-01,used=unknown,total=100"
hostname_part, rest = raw_line.split(",", 1)
for piece in rest.split(","):
    key, value = piece.split("=", 1)
    try:
        print(key, float(value))
    except ValueError:
        print(f"Could not convert {key}: {value}")
