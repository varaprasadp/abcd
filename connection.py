import sqlite3

def connect():
    conn = sqlite3.connect('postgres://gwvshgjceutpcf:6405b053099f7ae42afde62c180253c7a86cb43d3e134eb5a3366aee4a4ee47d@ec2-54-235-156-60.compute-1.amazonaws.com:5432/d10vqpdr1b33rr')
    conn.execute('CREATE TABLE IF NOT EXISTS database (name TEXT, age INTEGER, gender TEXT)')
    conn.close()

