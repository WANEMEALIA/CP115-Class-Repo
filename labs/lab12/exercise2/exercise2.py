score = float(input("Enter score (-1/101 to stop): "))
score_count = 0
total_score = 0
average_score = 0

# TODO: Your code here
while 0 < score < 101:
    score_count += 1 
    total_score += score
    average_score = total_score / score_count
    score = float(input("Enter score (-1/101 to stop): "))

print("Please enter score value in range 0 - 100 only.")
print(score_count)
print(total_score)
print(f"{average_score:.2f}")
