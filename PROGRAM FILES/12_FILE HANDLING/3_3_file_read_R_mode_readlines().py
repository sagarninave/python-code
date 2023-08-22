file = open("files/3_0_file_read_R_mode.txt", "r")
print("Reading Data of First Line Data\n")
data = file.readlines()
for x in data:
    print(x)
file.close()
