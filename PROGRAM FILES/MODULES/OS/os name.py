import os
from os import path
from datetime import time, date, timedelta
import time
import datetime
def main():
    print(os.name)
    print("Item exists " + str(path.isdir("foo.txt"))) # check it is directory or not
    print("Item exists " + str(path.isfile("foo.txt"))) # check it is file or not
    print("Item exists " + str(path.exists("foo.txt"))) # check path exists
    print("Item exists " + str(path.exists("foo1.txt"))) # check path does not exist

    print("path is : " + str(path.realpath("foo.txt"))) #full path of file
    print("path and file name : " + str(path.split(path.realpath("foo.txt")))) # saperate file path and file name

    mt1 = time.ctime(path.getmtime("foo.txt")) # achived from time package
    print(mt1)
    
    mt2 = datetime.datetime.fromtimestamp(path.getmtime("foo.txt")) # achived from datetime package
    print(mt2)

    mb = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("foo.txt"))
    print("Before " + str(mb) + " file has been modified")
    print("Before " + str(mb.total_seconds()) + " seconds file has been modified")
    
    x = path.isfile("foo.txt")
    x1 = True

    if x is x1:
        print("it is true")
    else:
        print("it is false")
    
if __name__ == "__main__":
    main()
