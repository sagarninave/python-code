class employee:
    empCount=0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        employee.empCount +=1

    def displayCount(self):
        print("Total Employee %d" %employee.empCount)
        
    def displayEmployee(self):
        print("Name : ", self.name, "\n" "Salary : ", self.salary)

emp1 = employee("sagar",1000)
emp1.displayEmployee()
emp1.displayCount()
print("\n")

emp1 = employee("sanket",2000)
emp1.displayEmployee()
emp1.displayCount()
print("\n")

emp1 = employee("shubham",2300)
emp1.displayEmployee()
emp1.displayCount()
print("\n")

emp1 = employee("samay",2100)
emp1.displayEmployee()
emp1.displayCount()
print("\n")
class Employee:
    'common base class for all employees'
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount += 1
    def displayCount(self):
        print("total employees %d" %Employee.empCount)
    def displayEmployee(self):
        print("name:",self.name, "salary:",self.salary)

emp1 = Employee("Nisha", 2000)
emp2 = Employee("Gauri", 5000)
emp1.displayEmployee() 
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)


