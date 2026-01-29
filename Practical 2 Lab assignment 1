# 1. Collect Vendor Information
name = input("Enter Vendor Name: ")
year = input("Enter Year of Association: ")
phone = input("Enter Contact Number: ")
email = input("Enter Email ID: ")

# 2. Collect Monthly Purchase Data
# We'll store these in a list
monthly_purchases = []

print(f"\nEnter monthly purchase amounts for {name}:")

for i in range(1, 13):
    amount = float(input(f"  Month {i}: Rs. "))
    monthly_purchases.append(amount)

# 3. Calculate Totals
total_annual = sum(monthly_purchases)
average_monthly = total_annual / 12

# 4. Generate the Annual Report
print("\n" + "="*40)
print("       ANNUAL PURCHASE REPORT")
print("="*40)
print(f"Vendor Name:  {name}")
print(f"Since Year:   {year}")
print(f"Contact:      {phone}")
print(f"Email:        {email}")
print("-" * 40)

# Displaying a summary of spending
print(f"Total Annual Purchase: Rs. {total_annual:,.2f}")
print(f"Average Monthly Spend: Rs. {average_monthly:,.2f}")
print(f"Highest Monthly Bill:  Rs. {max(monthly_purchases):,.2f}")
print(f"Lowest Monthly Bill:   Rs. {min(monthly_purchases):,.2f}")
print("="*40)
