# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 08:09:16 2018

@author: CUTY
"""
a=[25,14,49,76,38]
print(a)
x = int(input("Enter number to search: "))
for i in a:
    if i==x:
        break;
        
if i==x:
    print("Item found at position",a.index(i)+1)
else:
    print("Item Not Found")

