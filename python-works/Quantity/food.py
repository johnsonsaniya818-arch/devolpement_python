#show how many records in the nutrition data set

file_path="python-works\\Quantity\\Food_Nutrition_Dataset.csv.xls"

fr=open(file_path,"r")

import csv

reader=csv.DictReader(fr)

data=[r for r in reader]

#print(len(data))

#how many records have apple as food_item

count=0

for r in data:

    if(r.get("category")=="Apples"):

        count+=1

#print(count)

#which food item have more fat

d1={r.get("food_name"):r.get("fat")for r in data }


m1=max(d1.values())

print(m1)

li1=[k for k,v in d1.items()if v==m1]

print(li1)

#print the food_name that have vitamin c greater than 2

d2={r.get("food_name"):r.get("vitamin_c")for r in data if (r.get("vitamin_c"))>"5" }

#print(d2)

# print first 5 rows


# for r in data[::5]:

#     print(r)

#how many food_category have cake and pies

li1=[]

for r in data:

    if r.get("category")=="Cakes and pies":

        li1.append(r.get("food_name"))

#print(li1)

#print all categories of food_item

li1={r.get("food_name")for r in data}

#print(li1)

#food by category fruits

fruits = []

for r in data:
    
    if "fruits" in r.get("category").casefold():

        fruits.append(r.get("category"))

#print(fruits)

# Print the food name with the highest calories

d5={r.get("food_name"):r.get("calories")for r in data}

max1=max(d5.values())

li5=[k for k,v in d5.items() if v==max1]

print(li5)

#Find how many foods have vitamin C = 0

li9=[r.get("food_name")for r in data if (r.get("iron"))=="0.12"]

print((li9))
    