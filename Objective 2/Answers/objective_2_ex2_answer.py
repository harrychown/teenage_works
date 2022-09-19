#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Objective 2, Exercise 1, Personal Example Answer
Harry Chown
"""

# Example test data
"""
input_1 = 0, input_2 = 1, result = 1
input_1 = 0, input_2 = 0, result = 0
input_1 = 2, input_2 = 2, result = re-loop
input_1 = one, input_2 = one, result = invalid literal
input_1 = 1:space: , input_2 = 1:space: 

"""


correct_input = False
result = 0
while not correct_input:
    input_1 = int(input("Initial input. Please select either a 0 or a 1 "))
    input_2 = int(input("Second input. Please select either a 0 or a 1 "))
    if input_1 == 0 or input_1 == 1:
        if input_2 == 0 or input_2 == 1:
            if input_1 == 1 or input_2 == 1:
                result = 1
            print(result)
            correct_input = True

        