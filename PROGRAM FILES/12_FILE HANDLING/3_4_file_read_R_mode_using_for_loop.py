file = open("files/3_0_file_read_R_mode.txt", "r")
print("Reading Data By For Loop\n")
for x in file:
    print(x)
file.close()
