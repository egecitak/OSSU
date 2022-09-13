# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 22:53:02 2022

@author: Acer
"""

def square ( x ):
    """
    Input: x, an integer or a float
    Returns the square of the input
    
    """
    return x**2

def fourthPower(x):
    """
    Input: x is an integer or a float
    Returns x raised to its fourth power
    """
    return square(square(x))

print(fourthPower(2))
print(fourthPower(-3))
print(fourthPower(1.25))