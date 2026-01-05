
arr=[2,7,9,5]

# lis1=[num**3 for num in arr]

# print(lis1)

# lis2=[num *5 for num in arr]

# print(lis2)

evens=tuple(num for num in arr if num%2==0)

print(evens)

num_gt_five=[num for num in arr if num>5]

print(num_gt_five)