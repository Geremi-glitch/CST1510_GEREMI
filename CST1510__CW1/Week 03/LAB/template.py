"""Record Check - Cyber Security lane (Threshold tier).

Checks failed login attempts against the total number of login attempts.
"""

# FUNCTIONS
def status_of(percent):
    """Return the status for a percentage of the allowed limit."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


# INPUT
label = input("Enter source IP: ")
value = float(input("Enter failed logins: "))
limit = float(input("Enter total attempts: "))

# PROCESS
difference = value - limit
percent = (value / limit) * 100
status = status_of(percent)

# OUTPUT
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"  Failed logins : {value:g}")
print(f"  Total attempts: {limit:g}")
print(f"  Status        : {status}")
print("=" * 34)
