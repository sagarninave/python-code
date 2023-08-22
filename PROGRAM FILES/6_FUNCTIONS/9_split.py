life = 'learn earn job eat sleep'
print(life)
mylife = life.split()
print(mylife, "\n")

email = 'me.sagarninave@gmail.com'
print(email)
dotsplit = email.split('.')
print(dotsplit, "\n")

atsplit = dotsplit[1].split('@')
print(atsplit)
print(atsplit[0].split('r'))
print("\n")



mylist = "apple.banana.grapes"
x = mylist.split(".")
print(x, "\n")

mylist = "apple,banana,grapes"
x = mylist.split(",")
print(x, "\n")

mylist = "apple banana grapes"
x = mylist.split(" ")
print(x, "\n")

mylist = "apple+banana+grapes"
x = mylist.split("+")
print(x, "\n")

mylist = "apple+banana+grapes"
x,y,z = mylist.split("+")
print(x,y,z, "\n")
print(x)
print(y)
print(z)

