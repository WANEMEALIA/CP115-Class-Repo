import math

num = float(input("Enter a number: "))

square_root = math.sqrt(num)
square = num ** 2
cube = num ** 3
sine_value = math.sin(num)

print("Number entered:", num)
print("Square root: " , square_root)
print("Square (power of 2): " , square)
print("Cube (power of 3): " , cube)
print("Sine value (in radians): " , sine_value)