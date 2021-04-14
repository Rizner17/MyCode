#!/usr/bin/env python3

import sqlite3 #import the SQL lite library
conn = sqlite3.connect('test.db') #connects to the sql lite database named test
print("Opened database successfully")
# below, executes the creation of a table called 'Company' with the rows ID, NAME< AGE< ADDRESS< SALARY
conn.execute('''CREATE TABLE COMPANY 
 (ID INT PRIMARY KEY     NOT NULL,
 NAME           TEXT    NOT NULL,
 AGE            INT     NOT NULL,
 ADDRESS        CHAR(50),
 SALARY         REAL);''')
print("Table created successfully")
conn.close()

