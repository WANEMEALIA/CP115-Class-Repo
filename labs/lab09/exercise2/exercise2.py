#Tax calculator 
#Input
employee_name = input("Enter your name: ")
base_salary = float(input("Enter your base salary: "))
ot_hours = int(input("Enter your overtime hours: "))
tax_status = input("Enter your status: ")

#constant
ot = 35
epf = 0.11 
socso = 0.005

#Calculate ot pay
ot_pay = ot_hours * ot

#Total income bfore deducted
total_income = base_salary + ot_pay

#TODO your code here
if (tax_status == "Single") :
    if (total_income >= 5000) :
        tax_rate = "22%"
        tax = 0.22
    else :
        tax_rate = "18%"
        tax = 0.18
elif (tax_status == "Married") :
    if (total_income >= 6000) :
        tax_rate = "20%"
        tax = 0.2
    else :
        tax_rate = "15%"
        tax = 0.15
elif (tax_status == "Head") :
    if (total_income >= 5500) :
        tax_rate = "25%"
        tax = 0.25
    else :
        tax_rate = "19%"
        tax = 0.19

after_tax = total_income * (1-tax)

epf_deduction = total_income*epf
socso_deduction = total_income*socso

net_salary = after_tax - epf_deduction - socso_deduction

#Output
print(employee_name)
print(tax_rate)
print(f"RM {net_salary:.2f}")