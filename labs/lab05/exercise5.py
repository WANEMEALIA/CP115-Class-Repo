score1 = float(input("Enter Test Score 1: "))
score2 = float(input("Enter Test Score 2: "))
score3 = float(input("Enter Test Score 3: "))

total = score1 + score2 + score3
average = total / 3

print("Score 1: {:.2f}".format(score1))
print("Score 2: {:.2f}".format(score2))
print("Score 3: {:.2f}".format(score3))
print("Total Score: {:.2f}".format(total))
print("Average Score: {:.2f}".format(average))