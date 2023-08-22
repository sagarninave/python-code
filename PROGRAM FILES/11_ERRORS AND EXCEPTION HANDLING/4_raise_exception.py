"""
The raise statement allows the programmer to force a specific exception to occur.
The sole argument in raise indicates the exception to be raised.
This must be either an exception instance or an exception class
(a class that derives from Exception).
"""
try:  
    age = int(input("Enter the age?"))  
    if age<18:  
        raise ValueError;  
    else:  
        print("the age is valid")  
except ValueError:  
    print("The age is not valid")

