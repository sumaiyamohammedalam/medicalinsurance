# Interactive Medical Insurance Estimator

# Function to calculate insurance cost
def calculate_insurance(age, sex, bmi, num_of_children, smoker):
    return 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# Ask the user for their details
age = int(input("Enter age in years: "))
sex = int(input("Enter sex (0 for female, 1 for male): "))
bmi = float(input("Enter BMI: "))
num_of_children = int(input("Enter number of children: "))
smoker = int(input("Are you a smoker? (0 for no, 1 for yes): "))

# Calculate base insurance cost
insurance_cost = calculate_insurance(age, sex, bmi, num_of_children, smoker)
print("\nThis person's insurance cost is $" + str(insurance_cost))

# Interactive exploration: changing age
age_change = int(input("\nIncrease age by how many years to see the effect? "))
new_insurance_cost = calculate_insurance(age + age_change, sex, bmi, num_of_children, smoker)
print("The change in cost after increasing age by " + str(age_change) + " years is $" + str(new_insurance_cost - insurance_cost))

# Changing BMI
bmi_change = float(input("\nIncrease BMI by how much to see the effect? "))
new_insurance_cost = calculate_insurance(age, sex, bmi + bmi_change, num_of_children, smoker)
print("The change in cost after increasing BMI by " + str(bmi_change) + " is $" + str(new_insurance_cost - insurance_cost))

# Changing sex
sex_change = int(input("\nChange sex? (0 for female, 1 for male): "))
new_insurance_cost = calculate_insurance(age, sex_change, bmi, num_of_children, smoker)
print("The change in cost for being sex " + str(sex_change) + " instead of " + str(sex) + " is $" + str(new_insurance_cost - insurance_cost))

# Changing smoker status
smoker_change = int(input("\nChange smoker status? (0 for non-smoker, 1 for smoker): "))
new_insurance_cost = calculate_insurance(age, sex, bmi, num_of_children, smoker_change)
print("The change in cost for being a smoker? " + str(smoker_change) + " is $" + str(new_insurance_cost - insurance_cost))

# Changing number of children
children_change = int(input("\nIncrease number of children by how many? "))
new_insurance_cost = calculate_insurance(age, sex, bmi, num_of_children + children_change, smoker)
print("The change in cost after adding " + str(children_change) + " children is $" + str(new_insurance_cost - insurance_cost))
