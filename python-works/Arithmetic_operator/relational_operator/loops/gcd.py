
num1=int(input("enter a number "))#6

num2=int(input("enter the second number "))#12

small=min(num1,num2)#6

gcd=0

for i in range(1,small+1):#1 to 6

    if(num1%i==0 and num2%i==0):#6%1==0 and 12%1==0 6%2==0,12%2==0,6%3==0,12%3==0,6%4==0

        gcd=i #1,2,3

print(i)