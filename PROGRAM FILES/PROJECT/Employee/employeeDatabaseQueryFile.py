import sqlite3
con = sqlite3.connect("empolyeeDatabase.db")
c = con.cursor()

################# CREATE TABLE
# c.execute(""" CREATE TABLE employee(
#               acc_id NUMERIC PRIMARY KEY UNIQUE NOT NULL, 
# 		fname VARCHAR NOT NULL,
# 		lname VARCHAR NOT NULL,
# 		address TEXT NOT NULL,
# 		age INTEGER NOT NULL,
# 		salary NUMERIC NOT NULL,
# 		Join_date VARCHAR NOT NULL,
# 		dept_id INTEGER NOT NULL,
# 	        CONSTRAINT FK_DEPARTMENT FOREIGN KEY(dept_id) REFERENCES department(dept_id)
# 		)""")


# c.execute(""" CREATE TABLE department(
# 					dept_id INTEGER PRIMARY KEY UNIQUE NOT NULL, 
# 					dept_no INTEGER UNIQUE NOT NULL,
# 					dept_name VARCHAR NOT NULL,
# 					description TEXT NOT NULL)
# 					""" )


#c.execute("""INSERT INTO department VALUES('2','34', 'civil', 'it is a constructions related department');""")
#c.execute("""INSERT INTO employee VALUES('15555','sagar', 'ninave', 'Timki, nagpur', '23', '10000', '01 july 2019', '1');""")

################# ADD COLUMN INTO TABLE
# c.execute(""" ALTER TABLE employee DROP join_date VARCHAR""")

################# SELECT DATA

c.execute(""" SELECT * FROM employee """)
print(c.fetchall())
print("\n")

c.execute(""" SELECT * FROM department """)
print(c.fetchall())
print("\n")

c.execute(""" SELECT employee.fname, employee.dept_id, department.dept_name, employee.dept_id FROM employee inner join department on employee.dept_id = department.dept_id """)
print(c.fetchall())
print("\n")


con.commit()
con.close()
