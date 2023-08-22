import shutil
import os
from os import path
from shutil import make_archive
from zipfile import ZipFile

def main():
    # check file exist
    if path.exists("foo.txt"):
        print("hello")
        
        # get file path from current directory
        src = path.realpath("foo.txt")
    
        # creting backup copy by appending .bak 
        des = src + ".bak"
    
        #copy file by src parameter and appending name by des parameter 
        shutil.copy(src, des)
        shutil.copystat(src, des)
    
        # rename the original file
        os.rename("foo.txt", "foo1.txt")
    
        # put files into zip
        root_dir, tail = path.split(src)
        shutil.make_archive("archive", "zip", root_dir)

        with Zipfile("archive.zip", "w") as newzip:
            newzip.write("D:\PRACTICE CODE\PYTHON\PROGRAM FILES\MODULE\myfiel.py")
if __name__ == "__main__":
    main()