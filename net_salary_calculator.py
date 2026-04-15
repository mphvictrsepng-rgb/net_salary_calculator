# ---------------------------------------------------------
# PYTHON CHALLENGE: THE NET SALARY CALCULATOR (SARS 2026/27)
# ---------------------------------------------------------

# QUESTION 1: 
# Create three variables to get user input (floats):
# - monthly_gross_salary
# - medical_aid_premium
# - num_dependents (for medical credits)


# QUESTION 2:
# Calculate the monthly UIF contribution. 
# Remember: It is 1% of gross salary, but it is capped at R177.12.
# Hint: Use an 'if' statement or the min() function.


# QUESTION 3:
# To calculate tax (PAYE), we need the annual salary.
# Create a variable 'annual_gross' by multiplying monthly salary by 12.


# QUESTION 4:
# Using the 2026/27 Tax Brackets, create an if/elif/else structure
# to calculate the 'base_tax' on the 'annual_gross'.
# Example: 
# If income <= 245100, tax is 18%.
# If income > 245100 and <= 383100, tax is 44118 + 26% of amount above 245100.


# QUESTION 5:
# Everyone gets a Primary Rebate of R17,820 per year.
# Subtract this rebate from your 'base_tax'. 
# Note: Tax cannot be less than zero!


# QUESTION 6:
# Medical Tax Credits (MTC) reduce your tax.
# For 2026, the main member gets R376 off per month.
# Calculate the 'monthly_tax' by dividing annual tax by 12, 
# then subtract the R376 credit.


# QUESTION 7:
# Final Step! Calculate the 'net_salary'.
# Formula: Gross - Monthly Tax - UIF - Medical Aid Premium.


# QUESTION 8:
# Print a professional payslip showing:
# Gross Salary, UIF Deduction, Tax Paid, and the final Net Salary.