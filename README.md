# Practicals--C
To upload lab assignments1.
# 1. Get user input
name = input("Enter Name: ")
emp_id = input("Enter Employee ID: ")
dept = input("Enter Department: ")
basic = float(input("Enter Basic Salary: "))

# 2. Calculate the components
# Conditions: DA 92%, HRA 58%, TA 30%
da = basic * 0.92
hra = basic * 0.58
ta = basic * 0.30

# Deductions
lic = 500

# 3. Final totals
gross_salary = basic + da + hra + ta
net_salary = gross_salary - lic

# 4. Show the results
print("\n--- Employee Salary Details ---")
print(f"Employee: {name} ({emp_id})")
print(f"Dept:     {dept}")
print("-" * 30)
print(f"Basic:    Rs. {basic}")
print(f"DA:       Rs. {da}")
print(f"HRA:      Rs. {hra}")
print(f"TA:       Rs. {ta}")
print(f"LIC:    - Rs. {lic}")
print("-" * 30)
print(f"NET PAY:  Rs. {net_salary}")
