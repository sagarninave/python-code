filetype = ".doc"
file = input('Please enter the filename : ')
filename = file+filetype
fhandler = open("files/"+filename,'a+')
element_number = int(input('Enter Element Numbers : '))

for x in range(element_number):
    data = int(input("Enter Numbers: "))
    fhandler.write(str(data))
fhandler.seek(0)
print(fhandler.read(),"\n")
fhandler.close()
