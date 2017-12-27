'''Ch9 . Ex3: Write a program to read through a mail log, build a histogram using a dictionary to count 
how many messages have come from each email address, and print the dictionary.
'''

fhand = open('mbox-short.txt')
d = dict()
for line in fhand:
    if line.startswith('From ') is False: continue
    else:
        words = line.split()
        val = words[1]
        d[val]=d.get(val,0)+1
lst = d.keys()
for key in lst:
    print(key,d[key])
