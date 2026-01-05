
# ask 5:
# Create a file with several names (each name on a new line). Write a Python program to read all names from the file and display the first and last character of each name.

file_path="Arithmetic_operator\\file\\names.txt"

fr=open(file_path,"r")

li1=[]

for line in fr:

    wrd=line.rstrip("\n")

    if wrd == "":              # skip empty lines
        continue

    first_char = wrd[0]
    last_char = wrd[-1]


    li1.append((first_char,last_char))

print(li1)