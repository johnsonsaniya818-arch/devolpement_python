
#Write a Python program to find the largest and smallest element in a list.

list1=[10,20,5,30]

largest=list1[0]

for num in list1:

    if num>largest:

        largest=num

print("largest element",num)

