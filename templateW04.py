"""
RECORD CHECK  -  my version
===========================

Name  :  Ouvarshi Varsha Chuttur
Lane  :  IT     
Date  :  15/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 
# your function(s) go here
def status_of(percent):
    """Return a status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90 :
        return "WARNING"
    else :
        return "OK"


def check_record(value, limit):
    """Calculate and return the difference, percentage, and status."""
    difference = value - limit
    percent = (value / limit) * 100
    status = status_of(percent)
    return difference, percent, status

def print_report(label, value, limit, difference, percent, status):
    """Print a formatted report for one record."""
    print ("=" * 34)
    print(f"RECORD CHECK - {label}")
    print ("=" * 34)
    print(f"Used      : {value:.2f}")
    print(f"Total     : {limit:.2f}")
    print(f"Free      : {difference:.2f}")
    print(f"Percent   : {percent:.2f}%")
    print(f"Status    : {status}")
    print ("=" * 34)

# ====================================================================== STORE
# 

def load_records(path):
    """Read records from a file and return them as dictionaries."""
    records = []

    with open(path, "r") as file:
        for line in file:
            label, value, limit = line.strip().split(",")

            record = {
                "label": label,
                "value": float(value),
                "limit": float(limit)
            }

            records.append(record)

    return records

# Load the records from the data file
records = load_records(r"C:\Users\versh\Downloads\CST1510\W04\record.txt.txt")
print(records)

# =============================================================== PROCESS + OUTPUT
# your loop goes here

# Create file to save the results

over_limit_count = 0

with open("results.txt", "w") as output_file:
    for record in records:
        difference, percent, status = check_record(record["value"], record["limit"])

        print_report(
            record["label"],
            record["value"],
            record["limit"],
            difference,
            percent,
            status
        )

        # Write label and status to the results file
        output_file.write(f"{record['label']}, {status}\n")

        if status == "OVER LIMIT":
            over_limit_count += 1

print(f"Total records OVER LIMIT: {over_limit_count}")
        

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
