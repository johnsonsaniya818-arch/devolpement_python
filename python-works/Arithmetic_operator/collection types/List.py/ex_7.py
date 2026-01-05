
# 10. Convert a list with duplicate values

# into a set to remove duplicates, then print the result.

numbers = [1, 2, 2, 3, 4, 4, 5]

num_1=[]

for i in numbers:

    if numbers.count(i)>1 and i not in num_1:

        num_1.append(i)

print(num_1)



