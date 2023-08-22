try:  
    fileptr = open("file.txt","r")    
    try:  
        fileptr.write("Hi I am good")  
    finally:  
        fileptr.close()  
        print("file closed")  
except:  
    print("Error") 


