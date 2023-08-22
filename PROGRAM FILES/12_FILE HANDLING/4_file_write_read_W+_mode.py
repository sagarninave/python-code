file = open("files/4_file_write_read_W+_mode.txt", "w+")
for x in range(10):
    file.write("This is Number " + str(x) + "\n")
file.seek(0)
print("Current Index Cursor Position Is On : " + str(file.tell()) + "\n")
print(file.read())
file.close()
