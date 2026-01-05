
weight_in_kg=int(input("enter your weight in kg"))

height_in_cm=int(input("enter your height"))

height_in_m=height_in_cm/100

bmi=weight_in_kg/(height_in_m**2)

bmi=round(bmi,0)

print(bmi)

if(bmi<20):

    print("you are under weight")

elif(bmi<25):

    print("you are normal weight")

elif( bmi<30):
   
    print("you are overweight")

elif(bmi>=30):

    print("you are obese")

else:

    print("invalid input")

