# Fixed: return the local value, then store it outside the function.
def check(value, limit):
    status = "OVER LIMIT" if value > limit else "OK"
    return status

status = check(87, 100)
print(status)
