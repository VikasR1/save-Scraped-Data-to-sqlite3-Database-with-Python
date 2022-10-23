import sqlite3

conn = sqlite3.connect('lunch.db')
c = conn.cursor()

# c.execute('''CREATE TABLE meals(sandwich TEXT, fruit TEXT, tablenumber INT)''')

#select all data from table and print
c.execute('''SELECT * FROM meals''')
results = c.fetchall()
print(results)