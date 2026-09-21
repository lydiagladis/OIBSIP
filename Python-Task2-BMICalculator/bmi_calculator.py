# BMI Calculator - Oasis Infobyte Internship
# Task 1: BMI Calculator

print("===== BMI CALCULATOR =====")

try:
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be greater than zero.")

    else:
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print("\n===== RESULT =====")
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")

except ValueError:
    print("Error: Please enter numbers only.")
