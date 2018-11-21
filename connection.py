import sqlite3
 def connect():
    conn = sqlite3.connect()
    conn.execute('CREATE TABLE IF NOT EXISTS database (name TEXT, age INTEGER, gender TEXT)')
    conn.close()
