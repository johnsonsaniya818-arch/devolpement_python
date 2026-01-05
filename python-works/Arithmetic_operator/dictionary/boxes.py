
treasure={"box1":"gold","box2":"silver","box3":"diamond","box4":"platinum"}

# print(treasure["box3"])

# treasure["box5"]="iron"

# print(treasure)

# if "box6" not in treasure:

#     treasure["box6"]="copper"

# print(treasure)

# for k in treasure:

#     print(k,treasure[k])

# for k in treasure:

#     print(k)

# for k in treasure.keys():

#     print("keys",k)

# for v in treasure.values():

#     print("values",v)

# for k,v in treasure.items():

#     print(k,v)

print(treasure.get("box10","empty"))#after we using get method to return the value of that key otherwise it returns none or other value we can give like this empty

print("task1")

print("task2")

print(treasure.pop("box4"))

print(treasure)



