class fruitveg:
    color="red"
    def getColor(self):
        print("color is ",self.color)
obj=fruitveg()
obj.getColor()
        
print("\n")

class student:
    def __init__(self,n,r,s):
        self.name=n;
        self.rollno=r;
        self.sem=s;
        
    def display(self):
        print("Student Name is :",self.name)
        print("Student roll no is :",self.rollno)
        print("Student semester is :",self.sem)
        print("\n")
obj=student("sagar","001","mca")
obj1=student("sanket","001","mca")
obj.display()
obj1.display()
            
            
            
