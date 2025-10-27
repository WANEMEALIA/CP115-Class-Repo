#Wanemealia. calculates and displays the amount of the bill to be paid based on monthly usage
monthly_usage = float(input("Enter monthly usage : "))

#Determining discount
if monthly_usage < 50 :
    discount = 0
elif monthly_usage <= 100 :
    discount = 0.05
else :
    discount = 0.2

    
#Calculating total bill
bill = monthly_usage - (discount * monthly_usage)

print(f"Amount of bill to be paid is RM {bill}")