# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 22:56:58 2022

@author: Acer
"""

def odd (x):
    """
    Parameters
    ----------
    x : integer

    Returns
    -------
    True if x is odd, 
    False otherwise.

    """
    if (x % 2 == 1):
        return True
    else:
        return False
    
print(odd(3))
print(odd(1.3))
print(odd(-3))