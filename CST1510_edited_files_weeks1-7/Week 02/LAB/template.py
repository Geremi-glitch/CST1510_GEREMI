"""Week 2 Record Check mini-project — Cyber Security lane (Threshold).

Ask for a source IP, failed-login count and total-attempt count, then
report whether failed logins are over the supplied limit.
"""

# INPUT: input() returns text; convert the two numeric values to floats.
source_ip = input("Source IP: ")
failed_logins = float(input("Failed logins: "))
total_attempts = float(input("Total attempts: "))

# PROCESS: use an if/else decision to choose the status.
if failed_logins > total_attempts:
    status = "OVER LIMIT"
else:
    status = "OK"

# OUTPUT: print the three supplied values and the status in a border.
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {source_ip}")
print("=" * 34)
print(f"  Failed logins : {failed_logins:g}")
print(f"  Total attempts: {total_attempts:g}")
print(f"  Status        : {status}")
print("=" * 34)
