# 1-5. Define the function to calculate insurance cost
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    # Calculate the estimated cost
    estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
    
    # Print a personalized message
    print(f"The estimated insurance cost for {name} is {estimated_cost} dollars.")
    
    # Return the cost in case we need to use it later
    return estimated_cost

# 6-8. Calculate insurance costs for Maria and Omar
maria_insurance_cost = calculate_insurance_cost("Maria", 28, 0, 26.2, 3, 0)
omar_insurance_cost = calculate_insurance_cost("Omar", 35, 1, 28.5, 2, 1)

# 12. Calculate your own insurance cost (example)
my_insurance_cost = calculate_insurance_cost("YourName", 30, 0, 24.7, 1, 0)

# Extra practice: optional function to calculate difference between two individuals
def insurance_cost_difference(cost1, cost2, name1, name2):
    difference = abs(cost1 - cost2)
    print(f"The difference in insurance cost between {name1} and {name2} is {difference} dollars.")
    return difference

# Example of using the difference function
insurance_cost_difference(maria_insurance_cost, omar_insurance_cost, "Maria", "Omar")
