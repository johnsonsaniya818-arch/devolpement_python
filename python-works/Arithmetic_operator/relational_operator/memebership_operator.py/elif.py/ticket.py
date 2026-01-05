
age=int(input("enter your age"))

if age in range(0,5):

    print("you have tickets free")

elif age in range(5,19):

    print("you have 10 rupees for ticket")

elif age in range(19,61):

    print("you have 20 rupees for tickets")

elif age in range(61,91):

    print("you have 10 rupees for your tickets")

else:

    print("invalid input")