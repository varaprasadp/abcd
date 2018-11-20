import sqlite3

def connect():
    conn = sqlite3.connect('ec2-54-235-156-60.compute-1.amazonaws.com')
    conn.execute('CREATE TABLE IF NOT EXISTS database (name TEXT, age INTEGER, gender TEXT)')
    conn.close()

