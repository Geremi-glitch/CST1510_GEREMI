"""Week 1 Record Check mini-project — Cyber Security lane."""

# Ask for the three values. input() returns text, so convert the numbers.
source_ip = input("Source IP: ")
failed_logins = int(input("Failed logins: "))
total_attempts = int(input("Total attempts: "))

# Print the values in a bordered report (Threshold requirement).
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {source_ip}")
print("=" * 34)
print(f"  Failed logins : {failed_logins}")
print(f"  Total attempts: {total_attempts}")
print("=" * 34)
