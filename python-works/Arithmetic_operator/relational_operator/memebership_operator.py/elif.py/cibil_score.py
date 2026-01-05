
cibil_score=int(input("enter your cibli score"))

if cibil_score in range(300,550):

    print("you are poor")

elif cibil_score in range(550,650):

    print("you are average")

elif cibil_score in range(650,750):

    print("you are good")

elif cibil_score in range(750,901):

    print("you are excellent")

else:

    print("invalid input")