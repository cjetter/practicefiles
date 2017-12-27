##
# Program to create dummy DB to test streaming latency in bokeh
##
import pandas as pd
import time as t
import sqlite3
from random import randrange, randint  ## TO BE DELETED

#create database
filepath='/Users/Apple/Documents/Programming/Python/Other Projects/Greenhouse/DHT_dummy_3.sqlite'
connection = sqlite3.connect(filepath)
cur = connection.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS LogData (DateTime TEXT PRIMARY KEY NOT NULL UNIQUE,
Humidity REAL NOT NULL,
Temperature REAL NOT NULL)''')

# create dummy data
start = '2016-07-24'
end = '2017-07-24'
time_series_temp = pd.date_range(start, end, freq='10min')
time_series_temp = time_series_temp.tolist()

for n in range(0,len(time_series_temp)):
    a = (str(time_series_temp[n].strftime("%m/%d/%Y %H:%M:%S")))
    b = randrange(40,80)/100
    c = randrange(25,50)
    cur.execute('''
INSERT INTO LogData (DateTime, Temperature, Humidity)
VALUES ( ?, ?, ?)''', (a, b, c))

#add reading to database
connection.commit()