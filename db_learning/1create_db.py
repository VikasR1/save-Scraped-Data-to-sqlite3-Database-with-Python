import sqlite3

# Task0 : create DB or access the existing DB
#the below command will be able to connect with existing db or create a new db
conn = sqlite3.connect('lunch.db')

#create a cursur object that will let us to interact with db using sql commands
#this will allow us to see commands and access the dabatase
c = conn.cursor()