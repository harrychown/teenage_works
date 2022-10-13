#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 10:48:09 2022

@author: f99731hc
"""
G = [["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]]

correctInput = False

while not correctInput:
    print("Select values using a zero-index 10x10 grid.")
    rowInput = int(input("Give row number for ship"))
    colInput = int(input("Give column number for ship"))
    posInput = input("Give orientation, horizontal or vertical?")
    
    if not (posInput == "H" and colInput > 7 and rowInput > 9) or  (posInput == "V" and rowInput > 7 and colInput > 9):
        correctInput = True
        

G[0][0] = "H"

print(G)