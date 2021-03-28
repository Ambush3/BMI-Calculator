print("Lets find your BMI")
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = weight/(height**2)

print("Your bmi is {0} and you are: ".format(bmi), end='')

if ( bmi < 18.5):
    print("underweight.")

elif ( bmi >= 18.5 and bmi < 25 ):
    print("normal weight.")

elif ( bmi > 25 and bmi < 30):
    print("slightly overweight")

elif ( bmi > 30 and bmi < 35):
    print("are obese.")

else:
    ( bmi > 35)
    print("clinically obese.")


