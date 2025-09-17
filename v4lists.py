names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# 1. Add a new individual
names.append("Priscilla")
insurance_costs.append(8320.0)

# 2. Combine names and insurance costs using zip
medical_records = list(zip(insurance_costs, names))

# 3. Print medical_records
print("Medical records:", medical_records)

# 4. Get the number of medical records
num_medical_records = len(medical_records)

# 5. Print number of medical records
print(f"There are {num_medical_records} medical records.")

# 6. Select the first medical record
first_medical_record = medical_records[0]

# 7. Print first medical record
print(f"Here is the first medical record: {first_medical_record}")

# 8. Sort medical_records by insurance cost (lowest first)
medical_records_sorted = sorted(medical_records)
print(f"Here are the medical records sorted by insurance cost: {medical_records_sorted}")

# 9. Get the three cheapest insurance costs
cheapest_three = medical_records_sorted[:3]
print(f"Here are the three cheapest insurance costs in our medical records: {cheapest_three}")

# 11. Get the three most expensive insurance costs
priciest_three = medical_records_sorted[-3:]
print(f"Here are the three most expensive insurance costs in our medical records: {priciest_three}")

# 13. Count the number of occurrences of "Paul"
occurrences_paul = names.count("Paul")
print(f"There are {occurrences_paul} individuals with the name Paul in our medical records.")
