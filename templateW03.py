"""
RECORD CHECK  -  my version
===========================

Name  : Ouvarshi Varsha Chuttur
Lane  :  IT      
Date  : 10/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
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
    """Calculate and return the difference and percentage."""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent


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


# Example record
label = "srv-01"
value = 87
limit = 120

difference, percent = check_record(value, limit)
status = status_of(percent)
print_report(label, value, limit, difference, percent, status)


# ==================================================================== INPUT
# 2. Ask for your three values.
#
over_count = 0

while True:
    label = input("Enter a hostname (or quit to stop): ")

    if label.lower() == "quit":
        break

    value = float(input("Enter amount used: "))
    limit = float(input("Enter Total: "))

# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
#
    difference, percent = check_record(value, limit)
    status = status_of(percent)

    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        over_count += 1



# =================================================================== OUTPUT
# 4. Print the report.
#
print("Number of records OVER LIMIT:", over_count)

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# your report lines go here

print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
