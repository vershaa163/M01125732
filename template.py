"""
RECORD CHECK  -  my version
===========================

Name  : Ouvarshi Varsha Chuttur
Lane  :  AI
Date  : 23/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#

# your class goes here
class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit


    def status(self):
        """returns a status based on the percentage"""
        percent = (self.value / self.limit * 100)

        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"



# ==================================================================== RECORDS
# 2. Create your records.
#

 # replace with your code
records = [
    Record("survey_2026", 1187, 1200),
    Record("survey_2027", 2000, 1600),
]

def load_records(path):
    """Load records from a file and return a list of Record objects."""
    records = []

    with open(path, "r") as file:
        for line in file:
            label, value, limit = line.strip().split(",")
            record = Record(label, float(value), float(limit))
            records.append(record)

        return records
# ==================================================================== OUTPUT
# 3. Print a report for each record.

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    # your report lines go here

    print("=" * 34)

records = load_records(r"C:\\Users\\versh\\Downloads\\CST1510\\W05\\Record_sample.txt")
        
for record in records:
    print(record.label, record.status())


over_limit_count = 0

# Print each record
for record in records:
    print("=" * 36)
    print(f"Dataset Name: {record.label}")
    print(f"Rows loaded: {record.value}")
    print(f"Rows expected: {record.limit}")

   
    status = record.status()
    print(f"Status: {status}")

   
    if status == "OVER LIMIT":
        over_limit_count += 1

# Print the total once
print("=" * 36)
print(f"Total records OVER LIMIT: {over_limit_count}")
# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
