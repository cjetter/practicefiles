'''Ch10Ex2: This program counts the distribution of the hour of the day for each of the messages. 
You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. 
Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.
'''

fhand = open('mbox-short.txt')
d = dict()

for line in fhand:
    if line.startswith('From ') is False: continue
    else:
        line = line.rstrip()
        words = line.split()
        timestamp = words[5]
        timestamp = timestamp.split(':')
        hour = timestamp[0]
        d[hour]=d.get(hour,0)+1

lst = list()
for key,val in list(d.items()):
    lst.append((key,val))
lst.sort()
#print(lst)
for x,y in lst:
    print x,y