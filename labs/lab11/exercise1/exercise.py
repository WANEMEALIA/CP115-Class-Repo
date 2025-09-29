# Multiple counters working together
day = 1
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

print(f"Week summary: RM{total_sales} total, {successful_days} successful days")