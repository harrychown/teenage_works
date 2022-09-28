# -*- coding: utf-8 -*-
"""
Objective 3 Exercise 1
By Harry Chown
"""

UserInput=input("Please select an ID number: ")
if len(UserInput) > 5:
    print("Please select value less than 10 digits")

UserInput=int(UserInput)
PasswordInput=input("Enter password: ")


correct_pass = False
while not correct_pass:
    AttemptID=int(input("Enter ID: "))
    AttemptPass=input("Enter password: ")
    if AttemptID != UserInput or AttemptPass != PasswordInput:
        print("Incorrect ID/password, please try again")
    else:
        print("Credentials correct...")
        correct_pass = True
    
    