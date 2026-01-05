
num1=int(input("enter a number "))#8

num2=int(input("enter a number "))#14

num3=int(input("enter a number "))#20

small=min(num1,num2,num3)#8


for i in range(1,small+1):

    if(num1%i==0 and num2%i==0 and num3%i==0):

        print(i)

    