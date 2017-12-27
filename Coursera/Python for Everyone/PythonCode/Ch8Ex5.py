'''Ch10Ex1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. 
Count the number of messages from each person using a dictionary. After all the data has been read, print the person with the
most commits by creating a list of (count, email) tuples from the dictionary. 
Then sort the list in reverse order and print out the person who has the most commits.
'''

fhand = open('mbox-short.txt')
d = dict()

for line in fhand:
    if line.startswith('From ') is False: continue
    else:
        line = line.rstrip()
        words = line.split()
        email = words[1]
        d[email]=d.get(email,0)+1

lst = list()
for key,val in list(d.items()):
    lst.append((val,key))
lst.sort(reverse=True)
val,key = lst[0]
print key, val