# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 22:10:03 2022

@author: Acer
"""
s = "zyxwvutsrqponmlkjihgfedcba"
maxLength = 0
tmpStr = ""

for i in range(len(s)):
    j = i
    k = j + 1
    count = 0
    while (k < len(s)):
        if (ord(s[j]) <= ord(s[k])):
            count += 1
            j += 1
            k += 1
        else:
            break
            
    if (count > maxLength):
        maxLength = count
        tmpStr = s[i: k]
    

if (maxLength == 0):
    tmpStr = s[0]

print("Longest substring in alphabetical order is: " + tmpStr)