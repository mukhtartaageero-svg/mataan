import sqlite3

conn = sqlite3.connect("mataan.db")

c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
password TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS messages(
id INTEGER PRIMARY KEY AUTOINCREMENT,
sender TEXT,
receiver TEXT,
message TEXT
)
""")

conn.commit()
conn.close()

print("Database Created ✅")
