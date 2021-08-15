import sqlite3
conn = sqlite3.connect('configs.db')
s_new = 6
conn.execute(f"UPDATE CONFIG set S={s_new} where ID = 1")
conn.commit()
cursor = conn.execute("SELECT * from CONFIG")
print(cursor.fetchall())
conn.close()