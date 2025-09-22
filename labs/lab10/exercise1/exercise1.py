position = input()
overtime_hours = int(input())
is_weekend = input()

bonus = 5
overtime_rate = 1.5
total_pay = 0
overtime_pay = 0

# Your code here
if is_weekend == "Yes" :
    overtime_pay = (overtime_hours*5) 
    if position == "Manager" :
        hourly_rate = 35
    elif position == "Supervisor" :
        hourly_rate = 25
    else :
        hourly_rate = 18
else : 
    overtime_pay = total_pay
    
total_pay = overtime_pay + hourly_rate

print(hourly_rate)
print(overtime_pay)
print(total_pay)