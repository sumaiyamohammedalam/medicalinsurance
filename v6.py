# cleaning medical data
medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Add your code here
# 2. Replace '#' with '$'
updated_medical_data = medical_data.replace("#", "$")
print("Updated medical data:\n", updated_medical_data)

# 3. Count the number of medical records
num_records = 0
for char in updated_medical_data:
    if char == "$":
        num_records += 1

print(f"There are {num_records} medical records in the data.")

# 6. Split the string into individual records
medical_data_split = updated_medical_data.split(";")
print("Split medical data:\n", medical_data_split)

# 7-8. Split each record by comma into a list
medical_records = []
for record in medical_data_split:
    medical_records.append(record.split(","))

print("Medical records as lists:\n", medical_records)

# 9-12. Clean up whitespace
medical_records_clean = []
for record in medical_records:
    record_clean = []
    for item in record:
        record_clean.append(item.strip())
    medical_records_clean.append(record_clean)

print("Cleaned medical records:\n", medical_records_clean)

# 14-15. Print names in uppercase
for record in medical_records_clean:
    record[0] = record[0].upper()
    print(record[0])

# 16-18. Store names, ages, BMIs, insurance costs in separate lists
names = []
ages = []
bmis = []
insurance_costs = []

for record in medical_records_clean:
    names.append(record[0])
    ages.append(record[1])
    bmis.append(record[2])
    insurance_costs.append(record[3])

print("Names:", names)
print("Ages:", ages)
print("BMIs:", bmis)
print("Insurance Costs:", insurance_costs)

# 19-21. Calculate average BMI
total_bmi = 0
for bmi in bmis:
    total_bmi += float(bmi)

average_bmi = total_bmi / len(bmis)
print(f"Average BMI: {average_bmi}")
