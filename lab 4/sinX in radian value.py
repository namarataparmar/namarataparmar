import math

def calculate_sin(x):
    return math.sin(x)

x = float(input("Enter the angle in radians: "))
result = calculate_sin(x)
print(f"sin({x}) = {result}")
