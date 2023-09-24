

height = float(input("What is your height (m)? "))
weight = float(input("What is your weight (kg)? "))

calc = round(weight/height**2)

if calc > 18.5:
    if calc < 25:
        print("your bmi is " + str(calc) + " normal weight")
    elif calc > 25 and calc < 30:
        print("your bmi is " + str(calc) + " slightly overweight")
    elif calc > 30 and calc < 35:
        print("your bmi is " + str(calc) + " obese")
    elif calc > 35:
        print("your bmi is " + str(calc) + " clincally obese")
else:
    print("your bmi is " + str(calc) + " underweight")
