import sqlite3

conn = sqlite3.connect('lunch.db')
c = conn.cursor()

c.execute('''CREATE TABLE meals(sandwich TEXT, fruit TEXT, tablenumber INT)''')
