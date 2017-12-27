'''Ch9 . Ex2:Write a program that categorizes each mail message by which day of the week the commit was done. 
To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. 
At the end of the program print out the contents of your dictionary (order does not matter).
Target Answer:
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
'''

fhand = open('mbox-short.txt')
d = dict()
for line in fhand:
    if line.startswith('From ') is False: continue
    else:
        words = line.split()
        val = words[2]
        d[val]=d.get(val,0)+1
print(d)
