item_name = input("Enter the item name: ")
price = float(input("Enter the price: "))

quantity = 3
tax_r = 0.06 

subtotal = price * quantity
tax = subtotal * tax_r
total = subtotal + tax

print("--- Receipt ---")
print("Item:", item_name)
print("Price per item: RM{:.2f}".format(price))
print("Quantity:", quantity)
print("Subtotal: RM{:.2f}".format(subtotal))
print("Tax (6%): RM{:.2f}".format(tax))
print("Total Cost: RM{:.2f}".format(total))