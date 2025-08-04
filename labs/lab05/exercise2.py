radius = float(input("Radius of a circle: "))
# Import entire modules
import math

# Using imported modules
A = math.pi*(radius**2)
roundA = round(A,2)
C = 2*math.pi*radius
roundC = round(C,2)

print("Area =" , roundA)
print("Circumference = " , roundC)