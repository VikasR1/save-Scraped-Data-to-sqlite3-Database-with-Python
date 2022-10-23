import sqlite3

conn = sqlite3.connect('lunch.db')
c = conn.cursor()

# c.execute('''CREATE TABLE meals(sandwich TEXT, fruit TEXT, tablenumber INT)''')

#data to insert
sandwich = 'apple'
fruit = 'mango'
tablenum = 21

# #insert and commit to database
# c.execute('''INSERT INTO meals VALUES(?,?,?)''', (sandwich, fruit, tablenum))
# conn.commit()

#select all data from table and print
c.execute('''SELECT * FROM meals''')
# c.execute('''SELECT fruit FROM meals''')
results = c.fetchall()
print(results)