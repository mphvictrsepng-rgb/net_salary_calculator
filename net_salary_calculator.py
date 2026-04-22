# ---------------------------------------------------------
# PYTHON CHALLENGE: THE NET SALARY CALCULATOR (SARS 2026/27)
# ---------------------------------------------------------

# QUESTION 1:
# Create three variables to get user input (floats):
# - monthly_gross_salary
monthly_gross_salary = float(input('insert gross salary: R'))
# - medical_aid_premium
medical_aid_premium = float(input('Medical aid premium: R'))
# - num_dependents (for medical credits)
num_dependents = int(input('How many dependents on your med aid?: '))
#print(f'your gross salary is R{monthly_gross_salary: .2f} while your medical aid premium is R{medical_aid_premium}')
#print(f'your gross salary is R{monthly_gross_salary: .2f} while your medical aid premium is R{medical_aid_premium}.', end=" ") #to mix two print() functions
print(f'QUESTION 1: Your gross salary is R{monthly_gross_salary: .2f} while your medical aid premium is R{medical_aid_premium}.', end=" ") #to mix two print() functions
print(f'Your number of dependents is {num_dependents}')

# QUESTION 2:
# Calculate the monthly UIF contribution. 
# Remember: It is 1% of gross salary, but it is capped at R177.12.
# Hint: Use an 'if' statement or the min() function.
UIF = float(monthly_gross_salary * 0.01)
if UIF > 177.12:
    print('QUESTION 2: UIF cap exceed')
else:
    print('QUESTION 2: UIF not exceeded')
# QUESTION 3:
# To calculate tax (PAYE), we need the annual salary.
# Create a variable 'annual_gross' by multiplying monthly salary by 12.
annual_gross = float(monthly_gross_salary * 12)
#PAYE = float(annual_gross * 0.18)
#print(f'Question 3: The PAYE is R{PAYE}')
annual_gross = monthly_gross_salary * 12
print(f'QUESTION 3: Annual Gross Salary: R{annual_gross:.2f}')

# QUESTION 4:
# Using the 2026/27 Tax Brackets, create an if/elif/else structure
# to calculate the 'base_tax' on the 'annual_gross'.
# Example: 
# If income <= 245100, tax is 18%.
# If income > 245100 and <= 383100, tax is 44118 + 26% of amount above 245100.
if annual_gross <= 245100:            # I used the current rates provided by SARS, data is located in the SARS website
    base_tax = annual_gross * 0.18

elif annual_gross <= 383100:
    base_tax = 44118 + (annual_gross - 245100) * 0.26

elif annual_gross <= 535600:
    base_tax = 80098 + (annual_gross - 383100) * 0.31

elif annual_gross <= 673000:
    base_tax = 127910 + (annual_gross - 535600) * 0.36

elif annual_gross <= 857900:
    base_tax = 177310 + (annual_gross - 673000) * 0.39

elif annual_gross <= 1817000:
    base_tax = 249270 + (annual_gross - 857900) * 0.41

else:
    base_tax = 644489 + (annual_gross - 1817000) * 0.45

print(f'QUESTION 4: Base Tax (Annual): R{base_tax:.2f}')

# QUESTION 5:
# Everyone gets a Primary Rebate of R17,820 per year.
# Subtract this rebate from your 'base_tax'. 
# Note: Tax cannot be less than zero!
primary_rebate = 17820
annual_tax = base_tax - primary_rebate

if annual_tax < 0:
    annual_tax = 0

print(f'QUESTION 5: Annual Tax after Rebate: R{annual_tax:.2f}')

# QUESTION 6:
# Medical Tax Credits (MTC) reduce your tax.
# For 2026, the main member gets R376 off per month.
# Calculate the 'monthly_tax' by dividing annual tax by 12, 
# then subtract the R376 credit.
monthly_tax = annual_tax / 12

mtc = 376  # medical tax credit per month
monthly_tax = monthly_tax - mtc

if monthly_tax < 0:
    monthly_tax = 0

print(f'QUESTION 6: Monthly Tax after Medical Credit: R{monthly_tax:.2f}')

# QUESTION 7:
# Final Step! Calculate the 'net_salary'.
# Formula: Gross - Monthly Tax - UIF - Medical Aid Premium.
net_salary = monthly_gross_salary - monthly_tax - UIF - medical_aid_premium

print(f'QUESTION 7: Your Net Salary is R{net_salary:.2f}')

# QUESTION 8:
# Print a professional payslip showing:
# Gross Salary, UIF Deduction, Tax Paid, and the final Net Salary.
print("\n------ PAYSLIP ------")
print(f"Gross Salary: R{monthly_gross_salary:.2f}")
print(f"UIF Deduction: R{UIF:.2f}")
print(f"Tax Paid (PAYE): R{monthly_tax:.2f}")
print(f"Medical Aid: R{medical_aid_premium:.2f}")
print(f"Net Salary: R{net_salary:.2f}")
print("---------------------")