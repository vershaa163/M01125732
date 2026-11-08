"""
RECORD CHECK  -  my version
===========================

Name  : Varsha Chuttur
Lane  :  AI 
Date  : 03/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

datasetname = input("Enter a dataset name: ")
rowsloaded = float(input("Enter number of rows loaded: "))
rowsexpected = float(input("Enter number of rows expected: "))

if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"

print("Dataset name:", datasetname)
print("Rows loaded:", rowsloaded)
print("Rows expected:", rowsexpected)
print("Available rows:", difference)
print("Percent of limit: {:.2f}%".format(percent))
print("Status:", status)


over_count = 0

while True:
    datasetname = input("Enter a dataset name (or quit to finish): ")

    if datasetname == "quit":
        break

    rowsloaded = float(input("Enter number of rows loaded: "))
    rowsexpected = float(input("Enter number of rows expected: "))

    difference = rowsexpected - rowsloaded
    percent = (rowsloaded / rowsexpected) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    print("Dataset name:", datasetname)
    print("Rows loaded:", rowsloaded)
    print("Rows expected:", rowsexpected)
    print("Available rows:", difference)
    print("Percent of limit: {:.2f}%".format(percent))
    print("Status:", status)

    if status == "OVER LIMIT":
        over_count += 1

print("OVER LIMIT records:", over_count)
