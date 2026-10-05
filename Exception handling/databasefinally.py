import sqlite3

try:
    a=sqlite3.connect("college.db")
    print("Database connected")
except Exception:
    print("Connection failed")
finally:
    a.close()
    print("Connection closed")