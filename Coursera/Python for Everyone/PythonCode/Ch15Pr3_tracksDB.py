import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('Ch15Pr3_tracksDB.sqlite')
cur = conn.cursor()

## Make some fresh tables using execute script
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    name TEXT UNIQUE
);
CREATE TABLE Genre (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    name TEXT UNIQUE
);
CREATE TABLE Album (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    artist_id INTEGER,
                    title TEXT UNIQUE
);
CREATE TABLE Track (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    title TEXT UNIQUE,
                    album_id INTEGER,
                    genre_id INTEGER,
                    len INTEGER, rating INTEGER, count INTEGER
);
''')

fname = input('Enter file name: ')
if len(fname)<1:fname = 'Library.xml'

### Example XML to be parsed
## <key>Track ID</key><integer>1015</integer>
# <key>Name</key><string>Tetherball(Revolutions1-3)</string>
# <key>Artist</key><string>METERMAIDS</string>
# <key>Album</key><string>NIGHTLIFE IN ILLINOISE</string>
# <key>Size</key><integer>10708114</integer>
# <key>Total Time</key><integer>267702</integer>
# <key>Play Count</key><integer>3</integer>
##		

def lookup(d, keyterm):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == keyterm :
            found = True
    return None

stuff = ET.parse(fname)
tracks = stuff.findall('dict/dict/dict')
print('Tracks in Library: ', len(tracks))

for track in tracks:
    if ( lookup(track, 'Track ID') is None ) : continue
    name = lookup(track, 'Name')
    artist = lookup(track, 'Artist')
    genre = lookup(track, 'Genre')
    album = lookup(track, 'Album')
    count = lookup(track, 'Play Count')
    rating = lookup(track, 'Rating')
    length = lookup(track, 'Total Time')

    if name is None or artist is None or genre is None or album is None : 
        continue

    #print(name, artist, album, count, rating, length)
    
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, album_id, genre_id, length, rating, count ) )

    conn.commit()

