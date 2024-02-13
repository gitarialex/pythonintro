marks=int(input("Enter Marks:"))

if marks>=80 and marks<=100:
    print("You have an A")
elif marks>=60 and marks<=79:
    print("You have a B")
elif marks>=40 and marks<=59:
    print("You have a C")
elif marks>=0 and marks<=39:
    print("You have failed")
else:
    print('Wrong Input')

# BMI Calculation

weight=float(input("Enter your weight in Kilograms"))
height=float(input("Enter your height in Metres"))
bmi=weight/(height**2)

if bmi<18.5:
    category="Underweight"
elif bmi>=18.5 and bmi<=24.9:
    category='Normal'
elif bmi>=25 and bmi<29.9:
    category="Overweight"
else:
    category="Obese"
print(f"Your BMI is {bmi:.2f} and you're classified as {category}")