# Task 1: Calculate Factorial Using a Function

userInput = int(input("Enter a number: "))

def factoriyal(n):
    if n < 2:
        return 1
    else:
        return n * (factoriyal(n-1))

result = factoriyal(userInput)
print(f"Factorial of {userInput} is:",result)


# Task 2: Using the Math Module for Calculations
import math

UserInput = float(input("Enter a number: "))

squrt_val = math.sqrt(UserInput)
log_val = math.log(UserInput)
sin_val = math.sin(UserInput)

print(f"Square root: {squrt_val}")
print(f"Logarithm: {log_val}")
print(f"Sine: {sin_val}")