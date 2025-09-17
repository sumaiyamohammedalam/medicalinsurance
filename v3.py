# with control flow

# Function to analyze smoker status
def analyze_smoker(smoker_status):
    if smoker_status == 1:
        print("To lower your cost, you should consider quitting smoking.")
    else:
        print("Smoking is not an issue for you.")

# Function to estimate insurance cost
def estimate_insurance_cost(name, age, sex, num_of_children, smoker):
    # Calculate insurance cost
    insurance_cost = 400 * age - 128 * sex + 425 * num_of_children + 10000 * smoker - 2500
    # Print personalized message
    print(f"The estimated insurance cost for {name} is ${insurance_cost} dollars.")
    # Analyze smoker status for advice
    analyze_smoker(smoker)
    # Return cost if needed
    return insurance_cost

# Example: Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost("Keanu", 29, 1, 3, 1)

# Your own insurance cost (example)
my_insurance_cost = estimate_insurance_cost("YourName", 30, 0, 1, 0)
