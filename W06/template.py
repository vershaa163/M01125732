"""
RECORD CHECK  -  my version
===========================

Name  : Ouvarshi Varsha Chuttur
Lane  : IT     
Date  :

Run it:   python template.py



"""

import pandas as pd

# ==================================================================== LOAD
df = pd.read_csv("records.csv")
df.head()
df.info()

# ================================================================= PROCESS
# your column(s) go here

df["percent"] = (df["value"] / df["limit"]) * 100
df["status"] = df["percent"].apply(lambda x: "OVER LIMIT" if x >= 100 else ("WARNING" if x >= 90 else "OK"))

# ================================================================== OUTPUT
print(df)
print(df[df["status"] != "OK"])
print(df.groupby("status").size())
df.to_csv("filename.csv", index=False)

import matplotlib.pyplot as plt

counts = df.groupby("status").size()

counts.plot(kind="bar")

plt.title("Count of Records by Status" , fontsize=12, fontweight='bold', color='red')
plt.xlabel("Status", fontsize=10, fontweight='bold')
plt.ylabel("Count", fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig("status_chart.png")
plt.show()

# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
