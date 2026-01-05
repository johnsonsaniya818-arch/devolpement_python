file_path="python-works\\Arithmetic_operator\\Error_handling\\even.txt\\eve.txt"

fr=open(file_path,"r")

li1=[]

li2=[]

dic1={}

li3=[]

for line in fr:

    line=line.rstrip("\n")

    try:
        
        num=int(line)

        li1.append(num)

    except Exception as e:

        continue

for num in li1:

    if num%2==0:

        li2.append(num)

#print(li2)

dic1={num:li2.count(num)for num in li2}

#print(dic1)

max_count=max(dic1.values())

#print(max_count)

li3=[k for k,v in dic1.items() if v==max_count]

print(li3)





