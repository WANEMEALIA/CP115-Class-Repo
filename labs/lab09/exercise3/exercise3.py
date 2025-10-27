day_type = input("Enter day: ")
show_time = int(input("Enter time: "))
customer_type = input("Enter customer type: ")
is_student = input("Are you a student ? : ")

price = 0
#your code here
if day_type == "Weekend":
    if customer_type == "Adult":
        price = 18
    elif customer_type == "Child":
        price = 12
    elif customer_type == "Senior":
        price = 15
    else:
        price = 0
elif day_type == "Weekday":
    if customer_type == "Adult":
        price = 15
    elif customer_type == "Child":
        price = 10
    elif customer_type == "Senior":
        price = 12
    else:
        price = 0
else:
    price = 0

"""# Determine base price using separate if statements (no nesting)
base_price = 0

# Weekend Adult pricing
if day_type == "Weekend" and customer_type == "Adult":
    base_price = 18

# Weekend Child pricing  
if day_type == "Weekend" and customer_type == "Child":
    base_price = 12

# Weekend Senior pricing
if day_type == "Weekend" and customer_type == "Senior":
    base_price = 15

# Weekday Adult pricing
if day_type == "Weekday" and customer_type == "Adult":
    base_price = 15

# Weekday Child pricing
if day_type == "Weekday" and customer_type == "Child":
    base_price = 10

# Weekday Senior pricing
if day_type == "Weekday" and customer_type == "Senior":
    base_price = 12"""


# Apply evening surcharge (after 6pm = show_time > 18)
if show_time >= 18:
    price += 3

# Apply student discount (10% off final price, weekdays only)
if day_type == "Weekday" and is_student == "Yes":
    price *= 0.9


print(price)
print(price)