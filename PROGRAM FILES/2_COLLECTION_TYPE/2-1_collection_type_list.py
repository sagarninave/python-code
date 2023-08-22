player = [10,20,30,40,50]
print("simple list: ", player)
print("\n")

player[1]=200
print("putting value at 2nd position\n",player)
print("\n")

print("putting value in 2nd posotion and adding elements ")
player[1] = 20
player1 = player + [60,70,80]
print(player1)
print(player + [60,70,80])
print("\n")

print("appending value in last position ")
player1.append(90)
print(player1)
print("\n")

print("showing first two elements ")
print(player1[:2])
print("\n")

print("changing first two elements ")
player1[:2] = [1.0, 2.0]
print(player1)
print("\n")

print("changing first third and fourth elements")
player1[2:4] = [3.0,4.0]
print(player1)
print("\n")

print("removing or not showing first two element and list starts from 3rd element ")
player1[:2] = []
print(player1)
print("\n")

print("removing or not showing next elements from first two element ")
player1[2:] = []
print(player1)
print("\n")

print("eleminating all elements")
player1[:] = []
print(player1)
print("\n")

print("showinh all elements")
newlist = [2,4,5,6,7,8,1]
string = ['sagar','sanket','onkar','shubham','aaja','angad', 'alok']
print(string[:])
print("\n")

x=[]
y=[False]
z=[2]
print("it is any in string list: ",any(string))
print("It is empty list in x list: ",any(x))
print("it has false value in y list: ",any(y))
print("it has value in z list: ",any(z))
print("\n")

print(len(string))
print("\n")

print(max(string))
print("\n")

print(min(string))
print("\n")

string.insert(1, "raja")
print(string)
print("\n")

string.append('aman')
string.append('aman')
print(string)
print("\n")

print(string.count('aman'))
print("\n")

print(string.index('onkar'))
print("\n")

string.sort()
print(string)
print("\n")

mylist=string.copy()
print("mylist",mylist)
print("\n")

mylist[0]='ninave'
print(mylist)
print("\n")

mylist.remove("raja")
print("remove: ",mylist)
print("\n")

del mylist[0]
print("delete: ",mylist)
print("\n")

mylist.pop(2)
print("pop: ",mylist)
print("\n")

print(mylist.clear())
print("\n")


