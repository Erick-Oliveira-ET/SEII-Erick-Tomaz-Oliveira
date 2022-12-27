import sqlite3

with open('schema.sql', 'r') as sql_file:
    sql_script = sql_file.read()

con = sqlite3.connect("database.db")

cur = con.cursor()

print(sql_script)

cur.execute(sql_script)

con.commit()
con.close()