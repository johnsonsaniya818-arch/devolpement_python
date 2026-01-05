
#Given a list fruits = ["apple", "banana", "cherry", "apple"],
#remove all duplicates and print the updated list.

fruits=["apple","orange","cherry","apple"]

unique=[]

for i in fruits:

    if i not in unique:

        unique.append(i)

print(unique)




