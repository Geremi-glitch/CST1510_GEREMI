"""Record Check - Cyber Security lane (Threshold tier).

Checks failed login attempts against the total number of login attempts.
"""

def check_record(value, limit):
    """Return the difference, percentage of limit, and status."""
    difference = value - limit
    percent = (value / limit) * 100 if limit != 0 else 0
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print a formatted report for one source IP record."""
    print("=" * 42)
    print(f"RECORD CHECK - {label}")
    print("=" * 42)
    print(f"Failed logins : {value:g}")
    print(f"Total attempts: {limit:g}")
    print(f"Difference    : {difference:g}")
    print(f"Percentage    : {percent:.1f}%")
    print(f"Status        : {status}")
    print("=" * 42)


# STORE: Threshold requires at least three records written directly in code.
records = [
    {"label": "10.0.0.5", "value": 12, "limit": 400},
    {"label": "10.0.0.9", "value": 395, "limit": 400},
    {"label": "10.0.0.12", "value": 425, "limit": 400},
]

# PROCESS + OUTPUT
for record in records:
    difference, percent, status = check_record(record["value"], record["limit"])
    print_report(record["label"], record["value"], record["limit"],
                 difference, percent, status)
