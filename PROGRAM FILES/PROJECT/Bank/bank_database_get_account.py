import sqlite3
con=sqlite3.connect('bank.db')
c=con.cursor()
c.execute("SELECT * FROM deposit")
print(c.fetchall())
con.commit()
con.close()
