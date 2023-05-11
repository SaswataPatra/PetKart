import sqlite3

conn = sqlite3.connect('petshop.db')


with open('schema.sql') as f:
    conn.executescript(f.read())
conn.commit()
conn.close()