
num=int(input("enter your number "))#345

count=0

while(num!=0):#345!=0 34!=0 3!=0 0!=0(condition is false)

    digit=num%10 #345%10=5 34%10=4 3%10=3

    count=count+1 #1 2 3

    num=num//10 #345//10=34 34//10=3 3//10=0

print(count)

