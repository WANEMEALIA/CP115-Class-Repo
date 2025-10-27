age_input = int(input("Enter age (type 'done' to stop): "))
age_count = 0
total_age = 0
average_age = 0

# TODO: Your code here
while 1 < age_input < 120 :
    age_count +=1 
    total_age += age_input
    average_age = total_age / age_count
    age_input = int(input("Enter age (type 'done' to stop): "))

print("Done filling age.")
print(age_count)
print(total_age)
print(f"{average_age:.2f}")
