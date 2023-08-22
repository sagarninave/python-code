################################ Dict 1
x_dict=dict()
print("1st way to define dict")
print("printing dictionery defined by dict(): ",x_dict)
print("\n")

################################ Dict 2
y_dict={}
print("2nd way to define dict")
print("printing initialzed dictionery: ",y_dict)
print("\n")

print("adding element in dict")
y_dict["fname"]="sagar"
y_dict["lname"]="ninave"
y_dict["age"]=22
print(y_dict)
print("\n")

print("printing dict element by get function:\n",y_dict.get("fname"))
print("\n")

################################ Dict 3
dict = {'Name': 'sagar', "Lname":"Ninave", 'Age': 7, 'Class': 'First', "mobile":"9657445206"}
print("3rd way to define dict:\nx_dict: ",dict)
print("Accessing Elements of dict")
print("age: ",dict['Age' ])
print("Name: ",dict['Name'])
print("\n")

dict['Age'] = 23 #updating age (first check key exist the assign value)
dict['School'] = "RCOEM" #adding school (it does not got key so it is adding)
print("Updating Elements of dict")
print("Updated Age: ", dict['Age'])
print("Updatd School: ",dict['School'])
print("\n")

print("dict_Items: ",dict.items())
print("\n")

print("dict_Keys: ",dict.keys())
print("\n")

print("dict_Values: ",dict.values())
print("\n")

del dict["Class"]
print("Deleting Element both key:value pair using of dict")
print("dict after deleting Name:\n",dict)
print("\n")

a=dict.pop("Age")
print("Poping Element both key:value pair using of dict")
print("poping age and return value:\n",a)
print("dict after poping Age:\n",dict)
print("\n")

print("dict before popitem()\n",dict)
dict.popitem() # it does pop single element of dict from last it is vice versa of append()
print("Poping Element Using popitem()\n",dict)
print("\n")

newdict=dict.copy() # copying dict in new variable
print("Copting dict to variable and defining new dict")
print("newdict: ",newdict)
print("\n")

update_dict = {}
update_dict.update(newdict)
print("update dict content of newidct ",update_dict)
print("\n")

dict.clear()
newdict.clear()
update_dict.clear()
print("dict: ",dict)
print("newdict: ",newdict)
print("update_dict: ",update_dict)
print("\n")

my_dict = {}.fromkeys(["number1","number2","age"],22)
print("printing mewly created dict\n",my_dict)
print("\n")

print(list(sorted(my_dict)))
print("\n")

my_dict.setdefault("number2") # number 2 is exist then key:pair value will not be create 
print("setdefault value: ", my_dict)
print("\n")

my_dict.setdefault("number3") # Number 3 is not exist then key:pair value will be create with by default None Value
print("setdefault value: ", my_dict)
print("\n")

my_dict.setdefault("number4", 420) # Number 4 is not exist then key:pair value will be create with value 420
print("setdefault value: ", my_dict)
print("\n")

for x in my_dict.items():
    print(x)
print("\n")

for key, value in my_dict.items():
    print(str(key)+" : "+str(value))
print("\n")

loop_dict1 = {x: x*x for x in range(11)}
print("creating list with integer key from 0-10 and  value is square of its integer key\n",loop_dict1)
print("\n")

for x in range(11, 21):
    loop_dict1[x] = x*x
print("Value Inserted By For Loop\n",loop_dict1)
print("\n")

loop_dict2 = {x: x*x for x in range(11) if x%2==0}
print("creating list with integer key from 0-10 which is even number and  value is square of its integer key\n",loop_dict2)
print("\n")

for x in range(11,21):
    if x%2==0:
        loop_dict2[x]=x*x
print("Value Inserted By For Loop\n",loop_dict2)
print("\n")
    
loop_dict3 = {x: x*x for x in range(11) if x%2==1}
print("creating list with integer key from 0-10 which is odd number and  value is square of its integer key\n",loop_dict3)
print("\n")

for x in range(11, 21):
    if x%2==1:
        loop_dict3[x]=x*x
print("Value Inserted By For Loop\n",loop_dict3)
print("\n")

print("check key or value is presented in dictionery or not",9 in loop_dict3)
print("check key or value is presented in dictionery or not",2 in loop_dict3)
print("\n")

