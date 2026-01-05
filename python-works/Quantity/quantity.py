file_path="python-works\\Quantity\\cart_items_100.csv"

fr=open(file_path,"r")

import csv

reader=csv.DictReader(fr)

data=[row for row in reader]


order_summary={}

for o in data:

    title=o.get("title")

    qty=int(o.get("quantity",0))
    if title not in order_summary:

        order_summary[title]=qty

    else:

        order_summary[title]+=qty

print(order_summary)

max_val=max(order_summary.values())

print(max_val)

li1=[k for k,v in order_summary.items() if v==max_val]

print(li1)

min_val=min(order_summary.values())

li2=[k for k,v in order_summary.items() if v==min_val]

print(li2)

users={}

for u in data:

    use=u.get("user")

    if use not in users:

        users[use]=1

    else:

        users[use]+=1

print(users)

max1=max(users.values())

li3=[k for k,v in users.items() if v==max1]

print(li3)

