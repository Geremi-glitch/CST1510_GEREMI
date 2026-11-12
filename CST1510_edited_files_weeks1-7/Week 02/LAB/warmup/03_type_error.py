# Fixed: input() returns text, so convert it to a number before comparing.

limit = 20
value = float(input("Value: "))

if value > limit:
    print("OVER")
else:
    print("OK")
