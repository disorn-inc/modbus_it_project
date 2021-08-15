import sqlite3

# Connect to sqlite database
conn = sqlite3.connect('configs.db')
# cursor object
cursor = conn.cursor()
# drop query
cursor.execute("DROP TABLE IF EXISTS CONFIG")

# create query
query = """CREATE TABLE TOPIC(
        ID INT PRIMARY KEY NOT NULL,
        TOPIC CHAR(50) NOT NULL);"""
        
query2 = """CREATE TABLE CONFIG(
        ID INT NOT NUll,
        KEY CHAR NOT NULL,
        VALUE CHAR NOT NULL)"""
cursor.execute(query)
cursor.execute(query2)


'''CREATE TABLE artist(
  artistid    INTEGER PRIMARY KEY, 
  artistname  TEXT
);
CREATE TABLE track(
  trackid     INTEGER,
  trackname   TEXT, 
  trackartist INTEGER     -- Must map to an artist.artistid!
);'''


# commit and close
conn.commit()
conn.close()