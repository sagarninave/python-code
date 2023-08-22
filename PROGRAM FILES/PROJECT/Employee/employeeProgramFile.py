from datetime import date
import sqlite3
import random

class employee:
    def __init__(self, acc_id, fname, lname, address, age, salary, join_date, dept_id):
        self.acc_id = acc_id
        self.fname = fname
        self.lname = lname
        self.address = address
        self.age = age
        self.salary = salary
        self.join_date = join_date
        self.dept_id = dept_id


    def get_emp(self):
        
        params = (acc_id, fname, lname, address, age, salary, join_date, dept_id)
        
        con = sqlite3.connect("empolyeeDatabase.db")
        c = con.cursor()
        c.execute("INSERT INTO employee VALUES(?,?,?,?,?,?,?,?)", params)

        con.commit()
        con.close()
         
acc_id = int(random.randint(1, 10000))
join_date = str(date.today())
fname = str(input("Enter First Name: "))
lname = str(input("Enter Last Name: "))
address = str(input("Enter Address: "))
age = int(input("Enter Age: "))
salary = int(input("Enter Salary: "))
dept_id = int(input("Enter Department Id: "))

emp_obj = employee(acc_id, fname, lname, address, age, salary, join_date, dept_id)
emp_obj.get_emp()


