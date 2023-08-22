import os

from_file = input("Enter Name Of Old File : ")
to_file = input("Enter Name Of New File : ")
os.rename("files/"+from_file, "files/"+to_file)
