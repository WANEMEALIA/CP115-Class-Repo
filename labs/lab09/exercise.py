"""# Stage 1: Basic grade calculation
marks = 85
total_marks = 100

percentage = (marks / total_marks) * 100
print(f"Student scored: {percentage}%")

# Adding basic decision making
marks = 45
total_marks = 100

percentage = (marks / total_marks) * 100
print(f"Student scored: {percentage}%")

# conditional statement
if percentage >= 60:
    print("Congratulations! You passed!")

# Stage 3: Complete pass/fail system
marks = 45  # Try both passing and failing grades
total_marks = 100

percentage = (marks / total_marks) * 100
print(f"Student scored: {percentage}%")

# Complete conditional with else
if percentage >= 60:
    print("Congratulations! You passed!")
else:
    print("Sorry, you failed. Better luck next time!")

# This doesn't work well for multiple grades
if percentage >= 90:
    print("Grade: A")
else:
    print("Grade: ?")  # What about B, C, D, F?"""
"""
# multiple conditions with elif
marks = 87
total_marks = 100
percentage = (marks / total_marks) * 100

print(f"Student scored: {percentage}%")

if percentage >= 90:
    print("Grade: A - Excellent!")
elif percentage >= 80:
    print("Grade: B - Good!")
elif percentage >= 70:
    print("Grade: C - Satisfactory!")
elif percentage >= 60:
    print("Grade: D - Pass!")
else:
    print("Grade: F - Fail!")
"""
"""
# if statement - always at the beginning
student_grade = 95

if student_grade >= 90:
    print("Excellent performance")
""""""
# elif positioning - can have multiple elif statements
student_grade = 85

if student_grade >= 90:
    print("Excellent performance")
elif student_grade >= 80:    # After if
    print("Good performance") 
elif student_grade >= 70:    # After elif
    print("Satisfactory performance")
elif student_grade >= 60:    # After elif
    print("Minimum performance")"""
"""
# else positioning - always last
student_grade = 45

if student_grade >= 90:
    print("Excellent performance")
elif student_grade >= 80:
    print("Good performance")
elif student_grade >= 70:
    print("Satisfactory performance") 
elif student_grade >= 60:
    print("Minimum performance")
else:                        # Always positioned last
    print("Below minimum performance")
"""

# Multiple independent health checks - use multiple if statements
weight = 70  # kg
height = 1.75  # meters
age = 45
exercise_hours = 2  # per week

bmi = weight / (height * height)

# Each check is independent - multiple can be True
if bmi >= 25:
    print("Recommendation: Consider weight management")
    
if age >= 40:
    print("Recommendation: Schedule regular health checkups")
    
if exercise_hours < 3:
    print("Recommendation: Increase physical activity")
    
if bmi < 18.5:
    print("Recommendation: Consider increasing caloric intake")
