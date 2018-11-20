import sqlite3

def connect():
    conn = sqlite3.connect('d10vqpdr1b33rr')
    conn.execute('CREATE TABLE IF NOT EXISTS database (name TEXT, age INTEGER, gender TEXT)')
    conn.close()

