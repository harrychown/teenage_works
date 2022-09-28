# -*- coding: utf-8 -*-
"""
Objective 3 Exercise 3
By Harry Chown
"""

import random
correct_number = random.randint(0, 10)

incorrect = True

while incorrect:
    guess=int(input("Guess a random number between 0-10: "))
    if guess > correct_number:
        print("Too high, try again")
    elif guess < correct_number:
        print("Too low, try again")
    else:
        print("Congratulations, you are correct")
        incorrect = False