lst1=["10","20","hello","300","haii","2 00"]

li2=[]

for i in lst1:

    try:

        num=int(i)

        li2.append(num)

    except Exception as e:

        continue

print(li2)

max=max(li2)

min=min(li2)

sort=sorted(li2)

print(max)

print(min)

print(sort)
    

  



    




