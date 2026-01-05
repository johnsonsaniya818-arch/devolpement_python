num1=int(input("enter your number "))

num2=int(input("enter the second number "))

small=min(num1,num2)

for i in range(1,small+1):

    if(small%i==0):

        gcd=i

print(gcd)

