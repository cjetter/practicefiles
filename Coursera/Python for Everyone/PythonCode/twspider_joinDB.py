
import sqlite3

conn = sqlite3.connect('friends.sqlite')
cur = conn.cursor()

cur.execute('''SELECT * FROM Follows JOIN People
            ON Follows.to_id = People.id
            WHERE Follows.from_id = 1''')
count = 0
print('Connections for id=1:') 
for row in cur:
    if count < 20: print(row)
    count = count + 1
print(count, 'rows.')
cur.close()