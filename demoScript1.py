import sqlite3 as sql

conn = sql.connect("lite.db")
cur = conn.cursor()
cur.execute("CREATE TABLE  IF NOT EXISTS store (item TEXT,  quantity INTEGER, price REAL")
conn.commit()
conn.close()