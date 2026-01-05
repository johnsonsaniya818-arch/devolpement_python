
# Task 3:
# Create a text file containing several numbers. Write a Python program to read these numbers and display the last digit of each number.

file_path="Arithmetic_operator\\file\\last.txt"

fr=open(file_path,"r")

li1=[]

for line in fr:

    number=int(line.rstrip("\n"))

    num=number%10

    li1.append(num)

print(li1)