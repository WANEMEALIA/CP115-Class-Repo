age = int(input("Enter your age\n"))
ticket_price = float(input("Enter Ticket price\n"))
discount = 0
discount_category = ""

# Check invalid (negatives) value
if ticket_price < 0 :
    print ("INVALID TICKET PRICE, enter a positive number")
elif age < 0 :
    print ("INVALID AGE, enter a positive number")

# Determine discount based on age
else :
    if age <= 12 :
        discount_category = "Children"
        discount = 0.5
    elif age <= 17 :
        discount_category = "Teenagers"
        discount = 0.25
    else :
        discount_category = "Adults"
        discount = 0
# calculate discounted price
discounted_price = ticket_price - (ticket_price * discount)
# print output
print ("Discount Category :", discount_category)
print ("RM", discounted_price)