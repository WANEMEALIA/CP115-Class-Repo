#Movie ticket discount calculator program
#Input from user
age = int(input("Enter your age: "))
ticket_price = float(input("Enter the price of the movie ticket: "))
discount = 0
category = ""

#Checking whether age and ticket price are valid or not (must be positive value)
while age < 0 or ticket_price < 0 :
     print("Invalid input! Age and price of the ticket must be a positive value.")
     age = int(input("Enter your age: "))
     ticket_price = float(input("Enter the price of the movie ticket: "))


#Determining discount category based on age
if age <= 12:
    discount = 0.5
    category = "Children (50% discount)"
elif age <= 17:
    discount = 0.25
    category = "Teenagers (25% discount)"
elif age >= 18:
    discount = 0
    category = "Adults (No discount)"

# Process
final_price = ticket_price - (ticket_price * discount)

# Output
print(f"Discount Category: {category}")
print(f"Discounted ticket price: RM {final_price:.2f}\n")