import sqlite3

conn = sqlite3.connect('lunch.db')
c = conn.cursor()

#delete table
c.execute('''DROP TABLE meals''')