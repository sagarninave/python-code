my_file = open("files/bfile.bin", "wb+")
message = "Hello Python"
file_encode = message.encode("ASCII")
my_file.write(file_encode)
my_file.seek(0)
bdata = my_file.read()
print("Binary Data:", bdata)
ntext = bdata.decode("ASCII")
print("Normal data:", ntext)
