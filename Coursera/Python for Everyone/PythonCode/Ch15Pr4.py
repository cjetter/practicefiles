import sqlite3

conn = sqlite3.connect('Many2ManyDB.sqlite')
cur = conn.cursor()

cur.executescript('''
                DROP TABLE IF EXISTS Member;
                DROP TABLE IF EXISTS User;
                DROP TABLE IF EXISTS Course
                ''')

cur.executescript('''
                CREATE TABLE User (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT,
                email TEXT
                );
                CREATE TABLE Course (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                title TEXT 
                ) 
                ''')
conn.commit()
cur.executescript('''
                CREATE TABLE Member(
                user_id INTEGER,
                course_id INTEGER,
,
                PRIMARY KEY (user_id,course_id)    
                )
                ''')
conn.commit()