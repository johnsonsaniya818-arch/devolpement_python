
arr=[1,5,7,9,12,15,16,19,20]

count_even=0

count_odd=0

for i in arr:

    if i%2==0:

        print(i)

        count_even+=1

    else:

        print(i)

        count_odd+=1

print("----------------")

print(count_even)

print(count_odd)

