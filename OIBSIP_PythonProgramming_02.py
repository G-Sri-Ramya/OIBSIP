print("=== BMI Calculator ===")
try:
    height = float(input("Enter your height in meters : "))
    weight = float(input("Enter your weight in kilograms : "))
    if(height < 0.5 and height > 3):
        print("Enter valid height\n")
    if(weight < 0.5):
        print("Enter valid weight\n")
    bmi = weight / (height * height)
except ValueError:
    print("Enter Valid numbers\n")
print("BMI =",f"{bmi : .2f}")
if(bmi < 18.5):
    print("Under weight")
elif(bmi>=18.5 and bmi<=24.9):
    print("Normal weight")
elif(bmi>24.9 and bmi<=29.9):
    print("Over weight")
else:
    print("Obesity")
