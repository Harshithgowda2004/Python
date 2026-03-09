import sqlite3

conn = sqlite3.connect("arcade.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    score INTEGER DEFAULT 0
)
""")

conn.commit()
conn.close()