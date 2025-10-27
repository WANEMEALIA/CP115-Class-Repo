age = int(input())
accident_count = int(input())
base_premium = 0

# Your code here
if (age < 25):
    base_premium = 2400
if (age < 50):
    base_premium = 1800
else :
    base_premium = 2000

if accident_count == 0:
    penalty = 0
elif 1 <= accident_count <= 2:
    penalty = 300
else:
    penalty = 600

final_premium = base_premium + penalty
if accident_count == 0:
    discount_amount = final_premium*0.1
    final_premium -= discount_amount
else:
    discount_amount = 0


print(base_premium)
print(final_premium)
print(discount_amount)