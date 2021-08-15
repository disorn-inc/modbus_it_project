import sqlite3
conn = sqlite3.connect('configs.db')
# conn.execute("INSERT INTO CONFIG (ID,KEY,VALUE) "
#              "VALUES (1, 'size_too_large', '16')")
conn.execute("INSERT INTO TOPIC (ID,TOPIC) "
             "VALUES (1, 'crab_grader_1')")
            
conn.commit()
conn.close()