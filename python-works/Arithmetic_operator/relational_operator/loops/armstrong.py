
num=int(input("enter a number "))

is_armstrong=True

temp=num

count=0

sum=0

while(temp>0):

    digit=temp%10

    count+=1

    temp=temp//10

temp=num

while(temp>0):

    digit=temp%10

    sum=sum+(digit**count)

    temp=temp//10

if(sum!=num):

    is_armstrong=False

    print(is_armstrong)