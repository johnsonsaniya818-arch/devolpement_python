
employee={"id":1001,"name":"Saniya","department":"Devolper","location":"Thrissur","salary":50000}

print(employee)

print(employee["salary"])

print(employee["name"])

employee["phone"]=9400485745

print(employee)

employee["id"]=1005

print(employee)

if "email" in employee:

    print("exists")

else:

    employee["email"]="saniya@gmail.com"

print(employee)
