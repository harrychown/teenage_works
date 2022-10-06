# -*- coding: utf-8 -*-
"""
Objective 4 Exercise 3
By Harry Chown
"""

# List with numbers
numbers=[1,2,3,4,5]

# Generate a global variable to store the sum
sum_result = int()
# Iterate through the list to obtain values
for i in numbers:
    sum_result += i

# Calculate the mean
mean_result = sum_result / len(numbers)

# Calculate the highest and lowest values
max_result = max(numbers)
min_result = min(numbers)

# BONUS TRICK: Sum results using the sum function!
sum_result = sum(numbers)