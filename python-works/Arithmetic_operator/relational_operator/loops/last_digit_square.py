
num=int(input("enter your number"))

while(num!=0):

    last_digit=num%10

    print(last_digit**2)

    num=num//10