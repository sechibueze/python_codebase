import sqlite3
from urllib import request

conn = sqlite3.connect("scrapper")
cs = conn.cursor()
query = input("Search :")

sql = "INSERT INTO xx (title) VALUES (?)"
cs.execute(sql, [query])
conn.commit()

r = request.get()
html = r.text

with open()
