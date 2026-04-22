monthly_gross_salary = float(input('insert gross salary: R'))
print(f'monthly_gross_salary is R{monthly_gross_salary}')
uif = monthly_gross_salary * 0.01
if uif > 177.12:
    uif = 177.12

print(f"\nUIF Deduction: R{uif:.2f}")