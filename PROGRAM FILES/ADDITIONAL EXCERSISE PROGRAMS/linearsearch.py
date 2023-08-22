# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 08:16:12 2018

@author: CUTY
"""

list = [4, 9, 8, 0, 3, 7]


x = int(input("Enter number to search: "))

elementfound = False

for i in range(len(list)):
 if(list[i] == x):
  elementfound = True
  print("%d found at %dth position"%(x,i))

if(elementfound == False):
  print("%d is not in list"%x)
