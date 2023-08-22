default_age = 18
class voter:
    def voting(self, age):
        if age>=default_age:
            print("welcome To vote, Your age is " + str(age))
        else:
            print("You Are Not Aligible, Your age is " + str(age) + "\nYour age should be more than or Equal To " + str(default_age))
    
age = int(input("Enter Age : "))
v=voter()
v.voting(age)

print("\n")

a=15
b=10
c=12

if a>b and a>c:
    print("a is greater")
elif b>c:
    print("b is greater")
else: 
    print("c is greater")

    
if (a>b) and (a>c):
    print("a is greater")
elif ((b>a) and (b>c)):
    print("b is greater")
else: 
    print("c is greater")

    
 