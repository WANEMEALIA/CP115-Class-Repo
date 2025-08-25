test1 = 78
test2 = 85
test3 = 92
test4 = 67
test5 = 88

total = test1 + test2 + test3 + test4 + test5
avg = total / 5

full = 100

percentage1 = (test1/total) * 100
percentage2 = (test2/total) * 100
percentage3 = (test3/total) * 100
percentage4 = (test4/total) * 100
percentage5 = (test5/total) * 100

print(f"Test 1: {test1} \nTest 2: {test2} \nTest 3: {test3} \nTest 4: {test4} \nTest 5: {test5}")
print(f"Total points: {total}")
print(f"Average: {avg}")

print("\n===Percentage ===")
print(f"Test 1 : {round(percentage1,2)} %")
print(f"Test 2 : {round(percentage2,2)} %")
print(f"Test 3 : {round(percentage3,2)} %")
print(f"Test 4 : {round(percentage4,2)} %")
print(f"Test 5 : {round(percentage5,2)} %")