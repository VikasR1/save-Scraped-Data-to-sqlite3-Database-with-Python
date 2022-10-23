import sqlite3

# Task0 : create DB or access the existing DB
#the below command will be able to connect with existing db or create a new db
conn = sqlite3.connect('lunch.db')

#create a cursur object that will let us to interact with db using sql commands
#this will allow us to see commands and access the dabatase
c = conn.cursor()


# #delete table
# c.execute('''DROP TABLE meals''')

# Task1: create table in DB
# after creating a table, make sure to comment it out, 
# otherwise it will create table over and over again

# #create a table
# # and define columns and data type
# c.execute('''CREATE TABLE meals(sandwich TEXT, fruit TEXT, tablenumber INT)''')

#data to insert
sandwich = 'chicken'
fruit = 'orange'
tablenum = 22

# #insert and commit to database
# c.execute('''INSERT INTO meals VALUES(?,?,?)''', (sandwich, fruit, tablenum))
# conn.commit()

#select all data from table and print
c.execute('''SELECT * FROM meals''')
# c.execute('''SELECT fruit FROM meals''')
results = c.fetchall()
print(results)