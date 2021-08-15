import sqlite3
import pandas as pd


conn = sqlite3.connect('configs.db')
data = pd.read_sql('SELECT * from CONFIG', conn)
conn.close()

key = data.KEY

dict_data = pd.Series(data.VALUE.values,index=data.KEY).to_dict()
print(dict_data)

bg_upper = list(map(int,(dict_data['bg_upper'].split(','))))
bg_lower = list(map(int,(dict_data['bg_lower'].split(','))))
delay_camera = float(dict_data['delay_camera'])

print(bg_upper)
print(key)