#Task-2 
#Using math module to calculate the Square root of the number,
# Natural logarithm (log base e) of the number, 
# Sine of the number (in radians)
import math

# function to perform calculations
def calculate_values(num):
    if num <= 0:
        print("Number must be positive for square root and logarithm")
    
    sqrt_val = math.sqrt(num)    # Square 
    log_val = math.log(num)      # natural log (base e)
    sin_val = math.sin(num)      # sine in radians
    
    return sqrt_val, log_val, sin_val


number = int(input("Enter a positive number: "))

sqrt_val, log_val, sin_val = calculate_values(number)

print("Square root:", sqrt_val)
print("Natural log:", log_val)
print("Sine (radians):", sin_val)