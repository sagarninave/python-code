class mystack:
    stack_size=int(input("Enter the size of stack: "))
    top=-1
    stack=[]
    def push(self,a):
        if self.top>=self.stack_size:
            print("Stack is full")
        else:           
            self.top=self.top+1
            self.stack.append(a)
            print(a," is pushed in stack")
    def pop(self):
        if self.top==-1:
            print("Stack is empty")
        else:
            elem=self.stack[self.top]
            print("Element deleted is ",elem)
            self.top=self.top-1
            self.stack.remove(elem)
       
obj1=mystack()
'''obj1.push(2)
print(obj1.stack)
obj1.pop()
print(obj1.stack) '''   

print("\nMenu \n1.Push \n2.Pop \n3.Display stack \n0.Exit")
ans=''
while ans!='0':
    ans=input(" Enter your choice  ")
    if ans=="1":
        ele=input("Enter element to add : ")
        obj1.push(ele)        
    elif ans=="2":
        obj1.pop()
    elif ans=="3":
        print(obj1.stack)
    elif ans=="0":
        exit        
    else:
        print("Invalid choice, please choose again")
        print("\n")    
        

