file = open("files/2_file_append_A_mode.txt", "a")
for x in range(10):
    file.write(str(x)+"\n")
file.close()
