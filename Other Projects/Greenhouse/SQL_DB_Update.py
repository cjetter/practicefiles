import sqlite3
import datetime as dt
import pandas as pd

conn_DB = sqlite3.connect('DHT2.sqlite')
cur = conn_DB.cursor() 

df_original = pd.read_sql('SELECT * FROM LogData_orig',conn_DB)

# DT_list = list(df_original['Date'])
# Hum_list = list(df_original['Humidity'])
# Temp_list = list(df_original['Temperature'])


newDTlist = []

cur.execute('''SELECT * FROM LogData_orig
             ''')

DT_org = cur.fetchall()

for x in DT_org:
    if len(x[0])==19:
        newDTlist.append(x[0])
        continue
    #print(x[0])
    newDT = x[0]
    newDT = newDT.split(',')
    dt = '0' + newDT[0]
    tm = newDT[1]
    tm1 = tm.split(':')[0]
    if len(tm1)==1: tm1 = '0'+tm1
    tm2 = tm.split(':')[1]
    if len(tm2)==1: tm2 = '0'+tm2
    newT = tm1+":"+tm2+":00"
    newDT = dt+' '+newT
    #print(newDT)
    newDTlist.append(newDT)

df_original['Date'] = newDTlist

cur.executescript('''
                  CREATE TABLE IF NOT EXISTS LogData (DateTime TEXT PRIMARY KEY NOT NULL UNIQUE,Humidity REAL NOT NULL,Temperature REAL NOT NULL)
                  ''')
conn_DB.commit()

for dfrow in range(len(df_original)):
    inputs = list(df_original.iloc[dfrow])
    cur.execute('INSERT INTO LogData (DateTime,Humidity,Temperature) VALUES (?,?,?)',inputs)

conn_DB.commit()