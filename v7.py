# using python dictionaries

# 1. Create an empty dictionary
medical_costs = {}

# 2. Add two patients individually
medical_costs["Marina"] = 6607.0
medical_costs["Vinay"] = 3225.0

# 3. Add three patients in one line
medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})

# 4. Print the dictionary
print("Medical Costs Dictionary:")
print(medical_costs)

# 5. Update Vinay's insurance cost
medical_costs["Vinay"] = 3325.0
print("\nUpdated Medical Costs Dictionary:")
print(medical_costs)

# 6. Calculate total insurance cost
total_cost = 0
for cost in medical_costs.values():
    total_cost += cost

# 7. Calculate average insurance cost
average_cost = total_cost / len(medical_costs)
print(f"\nAverage Insurance Cost: {average_cost}")

# 8. Names and ages lists
names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]

# 9. Zip names and ages
zipped_ages = zip(names, ages)

# 10. Create dictionary using comprehension
names_to_ages = {name: age for name, age in zipped_ages}
print("\nNames to Ages Dictionary:")
print(names_to_ages)

# 11. Get Marina's age
marina_age = names_to_ages.get("Marina", None)
print(f"\nMarina's age is {marina_age}")

# 12. Create empty medical records dictionary
medical_records = {}

# 13. Add Marina's medical record
medical_records["Marina"] = {
    "Age": 27,
    "Sex": "Female",
    "BMI": 31.1,
    "Children": 2,
    "Smoker": "Non-smoker",
    "Insurance_cost": 6607.0
}

# 14. Add other individuals
medical_records["Vinay"] = {
    "Age": 24,
    "Sex": "Male",
    "BMI": 26.9,
    "Children": 0,
    "Smoker": "Non-smoker",
    "Insurance_cost": 3325.0
}

medical_records["Connie"] = {
    "Age": 43,
    "Sex": "Female",
    "BMI": 25.3,
    "Children": 3,
    "Smoker": "Non-smoker",
    "Insurance_cost": 8886.0
}

medical_records["Isaac"] = {
    "Age": 35,
    "Sex": "Male",
    "BMI": 20.6,
    "Children": 4,
    "Smoker": "Smoker",
    "Insurance_cost": 16444.0
}

medical_records["Valentina"] = {
    "Age": 52,
    "Sex": "Female",
    "BMI": 18.7,
    "Children": 1,
    "Smoker": "Non-smoker",
    "Insurance_cost": 6420.0
}

# 15. Print medical_records
print("\nMedical Records Dictionary:")
print(medical_records)

# 16. Print Connie's insurance cost
print(f"\nConnie's insurance cost is {medical_records['Connie']['Insurance_cost']} dollars.")

# 17. Remove Vinay from records
medical_records.pop("Vinay")

# 18. Print all patients' medical records nicely
print("\nFormatted Medical Records:")
for name, record in medical_records.items():
    print(f"{name} is a {record['Age']} year old {record['Sex']} {record['Smoker']} with a BMI of {record['BMI']} and insurance cost of {record['Insurance_cost']}")
