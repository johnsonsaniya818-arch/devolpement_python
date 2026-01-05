
weight_in_kg=int(input("enter your weight in kilograms "))

height_in_cm=int(input("enter your height in cm "))

height_in_m=height_in_cm/100

bmi=weight_in_kg/(height_in_m**2)

print(round(bmi,2))