"""A try statement can have more than one except clause,
to specify handlers for different exceptions.
Please note that at most one handler will be executed. """

try :  
    a = 3
    if a < 4 : 
          b = a/(a-3) 
    print("Value of b = ", b) 

except(ZeroDivisionError, NameError): 
    print("\nError Occurred and Handled\n")



try:
    fp = open('myfile.txt')
    line = f.readline()
    i = int(s.strip())
except (IOError,ValueError) as e:
    print ("Please check the file,either the file is read-only or the data can't be converted to an integer.",e.errno)
except:        #Note the use of except here,without any exception class, this can be used to handle all exception classes.
    print ("Unexpected error")
