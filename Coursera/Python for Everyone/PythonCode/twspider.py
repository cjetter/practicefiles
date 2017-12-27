
from urllib.request import urlopen
import urllib.error
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS Twitter
            (name TEXT, retrieved INTEGER, restricted TEXT, friends INTEGER)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('Enter a Twitter account, or quit: ')
    if (acct == 'quit'): break
    if (len(acct) < 1):
        cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
        try:
            acct = cur.fetchone()[0]
            print(acct)
            print(len(acct))
        except:
            print('No unretrieved Twitter accounts found')
            continue

    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)
    try:
        connection = urlopen(url, context=ctx)
    except:
        print('Account does not exist or is protected. Please try additional account.')
        cur.execute('UPDATE Twitter SET retrieved=1 WHERE name = ?', (acct, ))
        cur.execute('UPDATE Twitter SET restricted=? WHERE name = ?', ('yes',acct, ))
        continue
    data = connection.read().decode()
    headers = dict(connection.getheaders())

    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)
    # Debugging
    fhand = open('Jsondump.txt','w')
    fhand.write(json.dumps(js, indent=4))
    fhand.close()

    cur.execute('UPDATE Twitter SET retrieved=1 AND restricted=? WHERE name = ?', ('no',acct, ))

    countnew = 0
    countold = 0
    print(type(js))
    print(type(js['users']))
    print(len(js["users"]))
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1',
                    (friend, ))
        try:
            count = cur.fetchone()
            cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?',
                        (count+1, friend))
            countold = countold + 1
        except:
            cur.execute('''INSERT INTO Twitter (name, retrieved, restricted, friends)
                        VALUES (?, 0,'TBD', 1)''', (friend, ))
            countnew = countnew + 1
    print('New accounts=', countnew, ' revisited=', countold)
    conn.commit()

cur.close()