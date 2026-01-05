"""

3 Types of errors 

1.Syntax error

2.logical error

3.runtime error

blocks and keywords for handling

try except finally keywords assert raise

"""

# num1= int(input("enter a number"))

# num2=int(input("enter the second number"))

# try:

#     result=num1/num2

#     print(result)

# except Exception as e:

#     print(e)

# print("db committed")


file_path="finnallay//abc.txt"

try:

    fr=open(file_path,"r")

    for line in fr:

        print(line)

except Exception as e:

    print(e)

print("db committed")


