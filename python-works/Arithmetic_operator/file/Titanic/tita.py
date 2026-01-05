
file_path="Arithmetic_operator\\file\\Titanic\\dataset.csv"

fr=open(file_path,"r")

import csv

reader=csv.DictReader(fr)

data=[row for row in reader]

#print(data)

name=[r.get("Name")for r in data]

#print(name)

genders=[g.get("Sex")for g in data]

male_count=genders.count("male")

female_count=genders.count("female")

# print("male gender",male_count)

# print("female count",female_count)

survived_un_survived=[s.get("Survived")for s in data]

sur=survived_un_survived.count("1")

#print(survived_un_survived.count("0"))

#print(sur)

id=len(data)

#print(id)


no_of_passengers=[p.get("Pclass")for p in data ]

class_count={p:no_of_passengers.count(p) for p in no_of_passengers}

# print(class_count)

young_old=[int(a.get("Age"))for a in data if a.get("Age").isdigit()]

#print(young_old)

max1=max(young_old)

max2=min(young_old)

#print(max1)

#print(max2)

first_ten=data[:11]

first_ten_members=[p.get("Name")for p in first_ten]

#print(first_ten_members)

boarding_station=[s.get("Embarked")for s in data if len (s.get("Embarked"))>0]

bc={s:boarding_station.count(s) for s in boarding_station}

#print(bc)


passengers_age=[p for p in data if  p.get("Age").isdigit() and int(p.get("Age"))<10 ]

#print(len(passengers_age))

survived_children=[c for c in passengers_age if c.get("Survived")=="1"]

#print(len(survived_children))

survival_rate=[p for p in data if p.get("Survived")=="1"]

# sr=(len(survival_rate))

# all_passengers=len(data)

# print(all_passengers)

# sur_r=(sr/all_passengers)*100

# print(sur_r)

survived_male=[p for p in data if p.get("Survived")=="1" and p.get("Sex")=="male"]

survived_len=len(survived_male)

total_male=[p for p in data if p.get("Sex")=="male"]

total_male=len(total_male)

survived_rate_male=(survived_len/total_male)*100

#print("male",survived_rate_male)

survived_female=[p for p in data if p.get("Survived")=="1" and p.get("Sex")=="female"]

sur1_len=len(survived_female)

total_female=[p for p in data if p.get("Sex")=="female"]

t_female=len(total_female)

survived_rate_female=(sur1_len/t_female)*100

#print("female",survived_rate_female)


survived=[p.get("Pclass")for p in data if p.get("Survived")=="1"]

survived1={p:survived.count(p) for p in survived }

print(survived1)

no_of_passengers=[p.get("Pclass")for p in data ]

class_count={p:no_of_passengers.count(p) for p in no_of_passengers}

print(class_count)










