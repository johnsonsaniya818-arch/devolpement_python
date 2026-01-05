
db_pin=2456

db_balance=10000

pin=int(input("enter your pin"))

if(pin==db_pin):

    balance=int(input("enter your balance"))
    
    if(balance<db_balance):

        print("your amount is sufficient")
    else:
        print("you have insufficient balance amount")
else:

    print("incorrect pin")