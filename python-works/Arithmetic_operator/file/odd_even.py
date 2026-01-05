
# Create a text file containing a list of numbers (one number per line). 
# Write a Python program to read the numbers from the file and create two separate lists: 
# one list containing odd numbers and another list containing even numbers. Finally, display both lists.

file_path="Arithmetic_operator\\file\\numbers.txt"

li1=[]

li2=[]

fr=open(file_path,"r")

for line in fr:

    line=line.rstrip("\n")

    if line == "":            # skip blank lines
        continue

    number = int(line)     


    if number%2==0:

        li1.append(number)

    else:

        li2.append(number)

print(li1)

print(li2)

    