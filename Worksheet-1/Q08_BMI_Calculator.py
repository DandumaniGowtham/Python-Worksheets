def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    bmi = round(bmi, 2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "normal weight"
    elif bmi < 30:
        category = "overweight"
    else:
        category = "Obese"
    return {"bmi": bmi, "category": category}

weight = float(input("Enter weight: "))
height = float(input("Enter height in meters: "))
print(calculate_bmi(weight, height))
