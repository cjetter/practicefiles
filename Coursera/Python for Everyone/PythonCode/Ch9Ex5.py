'''Ch9 . Ex5: This program records the domain name (instead of the address) where the message was sent from 
instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

Target Answer:
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
'''

fhand = open('mbox-short.txt')
d = dict()
for line in fhand:
    if line.startswith('From ') is False: continue
    else:
        words = line.split()
        val = words[1]
        val = val.partition('@')
        val = str(val[2])
        d[val]=d.get(val,0)+1
lst = d.keys()
for key in lst:
    print(key,d[key])
