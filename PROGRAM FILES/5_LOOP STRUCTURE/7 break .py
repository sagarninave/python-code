number = int(input("Enter Number :"))

for i in range(101):
    if i is number:
        print(i , "is a number")
        break
    else:
        print(i)