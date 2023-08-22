# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 10:07:35 2018

@author: CUTY
"""

# Python program for implementation of bubble sort.
def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[64,34,25,12,11,90]
bubbleSort(arr)
print("sorted array is:")
for i in range(len(arr)):
    print("%d"%arr[i])