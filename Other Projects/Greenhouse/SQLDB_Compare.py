import sqlite3
import csv

# conn = sqlite3.connect('DHT2.sqlite')
# cur = conn.cursor()


# with open('output.csv', 'w') as f:
#     writer = csv.writer(f)
#     cur.execute('SELECT * FROM LogData')
#     data = cur.fetchall()
#     writer.writerows(data)

# conn.close()

# conn = sqlite3.connect('DHT2.sqlite')
# cur = conn.cursor()


# with open('output_org.csv', 'w') as f:
#     writer = csv.writer(f)
#     cur.execute('SELECT * FROM LogData_orig')
#     data = cur.fetchall()
#     writer.writerows(data)

# conn.close()

conn = sqlite3.connect('DHT2.sqlite')
cur = conn.cursor()


with open('output.txt', 'w') as f:
    cur.execute('SELECT * FROM LogData')
    data = cur.fetchall()
    for x in data:
        f.write(str(x[0])+'\t')
        f.write(str(x[1])+'\t')
        f.write(str(x[2])+'\t')
        f.write('\n')

conn.close()

conn = sqlite3.connect('DHT2.sqlite')
cur = conn.cursor()


with open('output_org.txt', 'w') as f:
    cur.execute('SELECT * FROM LogData_orig')
    data = cur.fetchall()
    for x in data:
        f.write(str(x[0])+'\t')
        f.write(str(x[1])+'\t')
        f.write(str(x[2])+'\t')
        f.write('\n')

conn.close()