friends = ['mahesh','ramesh','suresh']
print('Before',friends)
print(len(friends))
print(range(10))
friends[2] = 'radhika'
print('after',friends)
gfriends = ['radhika','sapna','Tina','megha','rohit','jigisha']

print(friends+gfriends)
print(gfriends[3:5])
print(gfriends[3:])
print(gfriends[:5])
print(gfriends[:])
print(dir(gfriends))

newString = "Hellofriendshowareyou"
print("New String\n",newString[0:20:2])

lfriends = list()
lfriends.append('sapna')
lfriends.append('apna')
lfriends.append('chupna')
lfriends.append('bolna')
print(lfriends)

if 'rukna' in lfriends:
    print('Hai')
else:
    print('Nahi hai')

lifepurpose = 'like$love$dokha'
mylife = lifepurpose.split('$')
print(mylife[2])

myemail = 'me.maheshrakheja@gmail.com'
val1 = myemail.split('.')
val2 = val1[1].split('@')
print(val2[0])
