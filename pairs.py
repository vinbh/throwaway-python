#!/usr/bin/env python3.8
import sqlite3
import csv
import os

cmd = """sqlite3 database.db <<< ".import /Users/vinayak.bhatt/Downloads/Airplane_Crashes_and_Fatalities_Since_1908.csv mytable" """

rc = os.system(cmd)

#print(rc)

conn = sqlite3.connect('database.db')
c = conn.cursor()

for row in c.execute('SELECT * FROM mytable limit 10'):
    print(row)
