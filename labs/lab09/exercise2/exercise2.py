#Tax calculator 
#Input
employee_name = input("Enter your name: ")
base_salary = float(input("Enter your base salary: "))
overtime_hours = int(input("Enter your overtime hours: "))
tax_status = input("Enter your status: ")

total_income = base_salary + (overtime_hours * 35)
epf = 0.11 * total_income
socso = 0.005 * total_income

taxable_income = total_income - epf - socso

# TODO your code here
if (tax_status == "Single") and (taxable_income >= 5000) :
    tax_rate = 0.22
else :
    tax_rate = 0.18
if (tax_status == "Married") and (taxable_income >= 6000) :
    tax_rate = 0.2
else :
    tax_rate = 0.15
if (tax_status == "Head") and (taxable_income >= 5500) :
    tax_rate = 0.25
else :
    tax_rate = 0.19

tax = taxable_income * tax_rate
net_salary = taxable_income - tax

#Output
print(employee_name)
print(tax_rate)
print(f"RM {net_salary:.2f}")