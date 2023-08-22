file = open("files/3_0_file_read_R_mode.txt", "r+")
print(file.read())
for x in range(10):
    file.write("This is Number " + str(x) + "\n")
file.seek(0)
print("Current Index Cursor Position Is On : " + str(file.tell()) + "\n")
print(file.read())
file.close()
