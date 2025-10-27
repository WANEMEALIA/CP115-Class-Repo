valid_count = 0
total = 0

# TODO: Your code here
while True:
    grade = float(input())
    
    # Stop reading if a negative number is entered
    if grade < 0:
       continue
    valid_count += 1
    total += grade

# Avoid division by zero
    if valid_count > 0:
        average = total / valid_count
    else:
        average = 0.0

print(valid_count)
print(f"{average:.2f}")
