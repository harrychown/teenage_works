# -*- coding: utf-8 -*-
"""
Objective 4 Exercise 5
By Harry Chown
"""

# Factors are two numbers that make a number
# For example, 24 has the following factors 1, 2, 3, 4, 6, 8, 12, 24


# Get a given number
UserNumber=int(input("Select a number: "))

# Generate a global variable to store results
factors = []

# Generate a nested FOR-loop to multiply all of the numbers up the user input against eachother to test whether or not it is a factor 
for num1 in range(1, UserNumber + 1):
    for num2 in range(1, UserNumber + 1):
        # BONUS STEP: Check to see if we have used num2 already
        if num2 in factors:
            continue
        # Multiply the two numbers
        result = num1 * num2
        # Store these numbers if they are a factor
        if result == UserNumber:
            factors.append(num1)
            factors.append(num2)
   
 # To work out if a number is a prime number it must only have two factors        
if len(factors) == 2:
    print("You have a prime number")