"""
RECORD CHECK  -  my version
===========================

Name  : Ouvarshi Varsha Chuttur
Lane  : IT
Date  : 07/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# your function(s) go here
def parse_line(raw_line):
    """Clean and parse one messy record line."""

    label, value, limit = raw_line.split(",") #separate the line into three parts
    label = label.strip().lower() #clean the label
    value = float(value.split("=")[1].strip()) #clean the value
    limit = float(limit.split("=")[1].strip()) #clean the limit

    return {"label": label, "used": value, "total": limit} #return the cleaned data as a dictionary

# def status_of(used, total):
def status_of(used, total):
    """Determine the status of a record based on its used and total values."""
    if used >= total:
        return "OVER LIMIT"
    elif used >= 0.90 * total:
        return "WARNING"
    else:
        return "OK"
    

# ====================================================================== INPUT

raw_records = [
    "  Srv-01 , used=87 , total=100  ",
    "SRV-02,used=120,total=100",
    "  srv-03,used=45 ,total=100",
    "Srv-04 , used = 93 , total=100",
    "  sRv-05, used=72,total = 100  "
]
for line in raw_records:
    record = parse_line (line)

record_count = 0
flagged_count = 0

# loop through the records in the file, parse them, and print their status
with open("records.txt", "r") as file:
    for line in file:
        record = parse_line(line)
        record_count += 1
        status = status_of(record["used"], record["total"])
        print(record, status)
        if status != "OK":
            flagged_count += 1

print(f"Records: {record_count}, Flagged: {flagged_count}")
           

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
