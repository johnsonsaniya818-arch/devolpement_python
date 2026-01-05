
num1=int(input("enter the first number "))

num2=int(input("enter the second number "))

num3=int(input("enter the third number "))

i=1

small=0

if(num1<num2 and num1<num3):

    small=num1

elif(num2<num1 and num2<num3):

    small=num2

else:

    small=num3

while(i<=small):

    if(num1%i==0 and num2%i==0 and num3%i==0):

        print(i)
    i+=1



