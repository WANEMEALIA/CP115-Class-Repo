#Tax calculator 
#Input
employee_name = input()
base_salary = float(input())
ot_hours = int(input())
tax_status = input()

#constant
ot_pay = ot_hours * 35

#Total income bfore deducted
total_income = base_salary + ot_pay

#TODO your code here
if tax_status == "Single" :
    if total_income >= 5000 :
        tax_charged = 0.22
        tax_rate_str = "22%"
    else :
        tax_charged = 0.18
        tax_rate_str = "18%"
elif tax_status == "Married" :
    if total_income >= 6000 :
        tax_charged = 0.2
        tax_rate_str = "20%"
    else :
        tax_charged = 0.15
        tax_rate_str = "15%"
elif tax_status == "Head" :
    if total_income >= 5500 :
        tax_charged = 0.25
        tax_rate_str = "25%"
    else :
        tax_charged = 0.19
        tax_rate_str = "19%"
else : 
    tax_charged = 0.0
    tax_rate_str = "0%"

net_salary = total_income * (1 - tax_charged) * (1 - 0.11) * (1 - 0.005)

#Output
print(employee_name)
print(tax_rate_str)
print(f"{net_salary:.2f}")