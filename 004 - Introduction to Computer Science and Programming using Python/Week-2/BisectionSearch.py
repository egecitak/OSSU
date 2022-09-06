# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 21:38:13 2022

@author: Acer
"""

high = 100
low = 0
ans = int((high + low) / 2)
choice = ""

print('Please think of a number between 0 and 100!')
choice = input('Is your secret number ' + str(ans) + "?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly." )

while (choice != "c"):
    if (choice == "h"):
         low = ans
    elif (choice == "l"):
        high = ans
    else:
        print('Sorry, I did not understand your input.')
 
    ans = round((high + low) / 2)
    choice = input('Is your secret number ' + str(ans) + "?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly." )

print('Game over. Your secret number was: ' + str(ans))