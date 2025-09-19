#Tax calculator 
#Input
employee_name = input("Enter your name: ")
base_salary = float(input("Enter your base salary: "))
overtime_hours = int(input("Enter your overtime hours: "))
tax_status = input("Enter your status: ")

total_income = base_salary + (overtime_hours * 35)
epf = 0.11 
socso = 0.005

# TODO your code here
if (tax_status == "Single") and (total_income >= 5000) :
    tax_rate = "22%"
    tax = 0.22
else :
    tax_rate = "18%"
    tax = 0.18
if (tax_status == "Married") and (total_income >= 6000) :
    tax_rate = "20%"
    tax = 0.2
else :
    tax_rate = "15%"
    tax = 0.15
if (tax_status == "Head") and (total_income >= 5500) :
    tax_rate = "25%"
    tax = 0.25
else :
    tax_rate = "19%"
    tax = 0.19

net_salary = total_income - ((tax*total_income)+(epf*total_income)+(socso*total_income))

#Output
print(employee_name)
print(tax_rate)
print(f"RM {net_salary:.2f}")