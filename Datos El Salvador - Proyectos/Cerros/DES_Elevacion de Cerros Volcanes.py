# Google Maps Elevation API - Cerros, Volcanes y Lomas en El Salvador 
#
# Author: Christopher Jetter
# Project: DATOS EL SALVADOR
'''
El objetivo de la presente es agregar los datos de elevación al repositorio de la ubicación geográfica de los cerros, volcanes y lomas en El Salvador. 
Para hacerlo, se utilizará el Google Maps Elevation API. 
'''

import csv
import urllib.error, urllib.request, urllib.parse
import json
import ssl
import sqlite3
import time

conn = sqlite3.Connection('DES_Elevacion_DB.sqlite')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS geodata (name TEXT, lat DECIMAL, lon DECIMAL, elev DECIMAL, PRIMARY KEY (name, lat,lon))')

with open('CERROS-VOLCANES-LOMAS-ELSALVADOR_0.csv', newline='') as f:
    reader = csv.reader(f)
    count = 0  
    for row in reader:
        count +=1
        name = row[0]
        lat = row[1]
        lon = row[2]
        if count == 1:continue
        cur.execute('INSERT OR IGNORE INTO geodata (name, lat, lon) VALUES (?,?,?)',(name, lat, lon))

conn.commit()

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = 'AIzaSyD4N_qkzZFoLTN4B1bXpzV-w9Vlu4hgx10'
serviceurl = 'https://maps.googleapis.com/maps/api/elevation/json?'

while True:
    varlist=[]
    x = cur.execute("SELECT * FROM geodata WHERE elev IS NULL")
    for item in x:
        varlist.append(item)

    try:
        name = varlist[0][0]
        lat = varlist[0][1]
        lon = varlist[0][2]
        print('Conseguiendo la elevacion de ', name,' ubicado en ',lat,' ',lon)
    except:
        print('No hay ningún registro con información pendiente.')
        quit()

    latlon = str(lat)+','+str(lon)

    parms = dict()
    parms["locations"] = latlon
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    headers = dict(uh.getheaders())
    print(headers)
    #print('Remaining', headers['x-rate-limit-remaining'])

    try:
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print('==== Failure To Retrieve ====')
        print(data)
        cur.execute('UPDATE geodata SET elev = ? WHERE name=? AND lat = ? AND lon=? ',('N/A',name,lat,lon))
        break

    elev = js["results"][0]["elevation"]
    print(elev,' meters')

    cur.execute('UPDATE geodata SET elev = ? WHERE name=? AND lat = ? AND lon=? ',(elev,name,lat,lon))
    conn.commit()