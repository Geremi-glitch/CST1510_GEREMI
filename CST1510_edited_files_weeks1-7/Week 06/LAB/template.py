"""Week 6 Record Check — Cyber Security lane (Threshold)."""

import pandas as pd

# Load the sample security records from the LAB folder.
df = pd.read_csv("security_records.csv")

# Calculate failed logins as a percentage of all attempts.
df["percent"] = (df["failed_logins"] / df["total_attempts"]) * 100

# Display the records and the calculated percentage.
print(df)
