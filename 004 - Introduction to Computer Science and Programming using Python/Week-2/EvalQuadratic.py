# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 15:51:27 2022

@author: Acer
"""

def evalQuadratic (a, b, c, x):
    """
    a, b, c: inputs are numerical values for quadratics
    x: value to evaluate the quadratic at
    """
    return a * x ** 2 + b * x + c

print (evalQuadratic(2, 2, 2, 2))