"""Cyber Security Record Check — Week 5 Threshold mini-project."""

# Lane: Cyber Security
# Name: add your name before submission
# Date: add the date before submission

class Record:
    """Store one security monitoring record."""

    def __init__(self, source_ip, failed_logins, total_attempts):
        self.source_ip = source_ip
        self.failed_logins = failed_logins
        self.total_attempts = total_attempts


# Create at least two records directly in the code.
records = [
    Record("10.0.0.5", 12, 400),
    Record("10.0.0.9", 95, 100),
    Record("10.0.0.12", 8, 120),
]

# Print a bordered report for each record using its attributes.
for record in records:
    print()
    print("=" * 38)
    print(f"  SECURITY RECORD - {record.source_ip}")
    print("=" * 38)
    print(f"  Failed logins : {record.failed_logins}")
    print(f"  Total attempts: {record.total_attempts}")
    print("=" * 38)
