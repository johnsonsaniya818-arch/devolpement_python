
file_path="Arithmetic_operator\\file\\perfect.txt"

fr=open(file_path,"r")

li1=[]

sum=0

for line in fr:

    number=int(line.rstrip("\n"))

    for i in range(1,number):

        if number%i==0:

            sum+=number

        if number==sum:

            li1.append(number)

print(li1)



