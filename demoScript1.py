import sqlite3 as sql
def create_table():
    conn = sql.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE  IF NOT EXISTS store (item TEXT,  quantity INTEGER, price REAL")
    cur.execute("INSERT INTO store VALUES('Chocolate', 8, 15.0)")
    conn.commit()
    conn.close()
