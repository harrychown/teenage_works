# -*- coding: utf-8 -*-
"""
Objective 3 Exercise 3
By Harry Chown
"""

import random


sixes = False
counter = 0
while not sixes:
    print("Rolling dice..")
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print(str(dice1)+","+str(dice2))
    counter += 1
    if dice1 == 6 and dice2 ==6:
        print("Congrats! It took you " + str(counter) + " attempts")
        sixes = True
    