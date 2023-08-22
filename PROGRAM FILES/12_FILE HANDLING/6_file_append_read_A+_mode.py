file = open("files/6_file_append_read_A+_mode.txt", "a+")
x = {x:x*x for x in range(1,11)}
file.write(str(x) + "new\n")
file.seek(0)
print(file.read())
file.close()
