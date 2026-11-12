"""
RECORD CHECK - Cyber Security lane
Week 7 mini-project: clean and parse messy security records.
"""

def parse_line(raw_line):
    """Clean one messy security record and return its fields as a dictionary."""
    cleaned_line = raw_line.strip().lower()
    fields = cleaned_line.split(",")
    record = {}

    for field in fields:
        key, value = field.split("=", 1)
        key = key.strip()
        value = value.strip()

        if key == "attempts":
            record[key] = int(value)
        else:
            record[key] = value

    return record


# Five deliberately messy records with different spacing and letter case.
raw_records = [
    " SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED ",
    "src = 10.0.0.8 , attempts = 3 , result = success",
    "  Src=192.168.1.20,Attempts=  7,Result=Blocked  ",
    "SRC = 172.16.0.4, ATTEMPTS=25 , RESULT = FAILED",
    "  src=10.10.0.9 ,attempts= 1,result=Success "
]

for raw_record in raw_records:
    cleaned_record = parse_line(raw_record)
    print(cleaned_record)
