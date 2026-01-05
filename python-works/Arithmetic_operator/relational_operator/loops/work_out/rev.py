num=int(input("enter a number "))

count=0

while(num>0):

    last=num%10

    count+=1

    num=num//10

print(count)

