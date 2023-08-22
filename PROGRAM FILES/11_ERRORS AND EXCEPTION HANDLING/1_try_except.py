a = [1, 2, 3] 
try:  
    print("Second element = {}".format((a[1]))) 
    print("Second element = {}".format((a[2]))) 
  
    # Throws error since there are only 3 elements in array 
    print("Fourth element = {}".format((a[3])))


except NameError: 
    print("An error occurred")
