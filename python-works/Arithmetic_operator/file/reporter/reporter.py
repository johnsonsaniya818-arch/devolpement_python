file_path="Arithmetic_operator\\file\\reporter\\reporter.csv"

fr=open(file_path,"r")

import csv

reader=csv.DictReader(fr)

data=[r for r in reader]

#print(data)

data1=len(data)

#print(data1)

# data2 = {r["BATCH"] for r in data}

#print(data2)

data3={r.get("NAME"):r.get("MCQ1")for r in data}

#print(data3)

data3={r.get("OVERALL")for r in data}

max1=max(data3)

#print(max1)

data4 = {
    r["NAME"]
    for r in data
    if any("-" in v for v in r.values())
}

#print(data4)

high_absent = [
    r for r in data
    if r["ABSENT_%"].replace("-", "").strip() != ""   # skip missing values
       and float(r["ABSENT_%"]) > 20
]

for student in high_absent:
    print(student)

