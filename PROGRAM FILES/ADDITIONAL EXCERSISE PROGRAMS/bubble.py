# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 08:03:05 2018

@author: CUTY
"""

def bubblesort(list):
    for i in range(len(list)):
        for j in range(len(list)-i-1):
            if list[j]>list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
list=[1,82,59,6,3,10]
bubblesort(list)
print(list)

