with open ("files/11_attributes.txt", "w") as f:

    print("File Mode Is: ",f.mode)
    print("File Name Is: ",f.name)
    print("File Is Writeable: ",f.writable())
    print("File Is Readable: ",f.readable())
    print("File Closed Is: ",f.closed)

    f.write("gello sagar")
    
print("File Closed Is: ",f.closed)
