grade = float(input("Enter grade : "))
valid_count = 0
total = 0
average = 0

#TODO: Your code here
while grade > 0:
    grade = float(input("Enter grade : "))
    valid_count += 1
    total += grade

    if grade < 0:
       print("Enter valid grade.")
       continue

# Avoid division by zero
    if valid_count > 0:
        average = total / valid_count
    else:
        average = 0

print(valid_count)
print(f"Grade average is : {average:.2f}")
