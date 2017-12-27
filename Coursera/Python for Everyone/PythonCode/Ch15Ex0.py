import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)') 

conn.close()

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',('Thunderstruck', 20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',('My Way', 15))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',('My Way2', 115))
#cur.execute('UPDATE Tracks SET plays = 150')
conn.commit()
print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks') 
for row in cur:
    print(row[1])
cur.execute('DELETE FROM Tracks WHERE plays < 20')
cur.execute('SELECT title, plays FROM Tracks') 
print('POSTDEL')
for row in cur:
    print(row)
print(conn)
cur.close()