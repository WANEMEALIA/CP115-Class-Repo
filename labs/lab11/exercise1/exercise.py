# Multiple counters working together
"""day = 1
total_sales = 0
successful_days = 0

print("Daily sales tracking:")
while day <= 7:  # One week
    daily_sales = float(input(f"Day {day} sales: RM"))
    total_sales += daily_sales

    if daily_sales >= 1000:
        successful_days += 1
        print(f"Day {day}: Target achieved!")
    else:
        print(f"Day {day}: Below target")

    day += 1

print(f"Week summary: RM{total_sales} total, {successful_days} successful days")"""

# Problem: Teacher must count students first!
"""num_students = int(input("How many students? "))
total = 0

for i in range(num_students):
    grade = float(input("Enter grade: "))
    total += grade

average = total / num_students
print(f"Average: {average}")"""

# Complete sentinel pattern - all three parts labeled
grade = float(input("Enter grade (-1 to stop): "))  # Part 1: Prime input

while grade != -1:  # Part 2: Condition
    print(f"You entered: {grade}")
    grade = float(input("Enter grade (-1 to stop): "))  # Part 3: Update input

print("Done entering grades!")